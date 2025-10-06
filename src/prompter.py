from __future__ import annotations

from typing import Optional

from langfuse import Langfuse
from openai import OpenAI
from openai.types.chat import ChatCompletion

from .settings import Settings


class Prompter:

    def __init__(self, base_url: str, api_key: str):
        self.base_url = base_url
        self.api_key = api_key
        self.client = OpenAI(base_url=base_url, api_key=api_key)
        self.langfuse = self._initialize_langfuse()

    def run(self, prompt: str) -> str:
        """ run prompt"""

        trace = None
        generation = None
        if self.langfuse:
            trace = self.langfuse.trace(
                name="prompter.run",
                input={"prompt": prompt},
                metadata={"base_url": self.base_url},
            )
            generation = trace.generation(
                name="prompter.chat_completion",
                model="main",
                model_parameters={
                    "temperature": 1,
                    "max_tokens": 8192,
                    "stream": False,
                    "stop": None,
                },
                input=prompt,
            )

        try:
            completion = self.client.chat.completions.create(
                model="main",
                messages=[{"role": "user", "content": prompt}],
                temperature=1,
                max_tokens=8192,
                stream=False,
                stop=None,
            )
        except Exception as exc:  # pragma: no cover - best effort logging
            if generation:
                generation.update(
                    level="ERROR",
                    status_message=str(exc),
                    metadata={"exception_type": type(exc).__name__},
                )
            if trace:
                trace.update(
                    level="ERROR",
                    status_message=str(exc),
                )
            raise

        content = self._extract_completion_content(completion)

        if generation:
            generation.update(
                output=content,
                usage=getattr(completion, "usage", None),
            )
        if trace:
            trace.update(output=content)

        return content

    @staticmethod
    def _extract_completion_content(completion: ChatCompletion) -> str:
        """Safely extract textual content from the Groq response."""
        if completion is None:
            return ""

        choices = getattr(completion, "choices", None)
        if not choices:
            return ""

        for choice in choices:
            message = getattr(choice, "message", None)
            if message is None and isinstance(choice, dict):
                message = choice.get("message")

            if message is None:
                continue

            if hasattr(message, "content"):
                content = message.content
                if content:
                    return content

            if isinstance(message, dict):
                content = message.get("content")
                if content:
                    return content

        return ""

    @staticmethod
    def _initialize_langfuse() -> Optional[Langfuse]:
        settings = Settings()
        public_key = (
            settings.LANGFUSE_PUBLIC_KEY.get_secret_value()
            if settings.LANGFUSE_PUBLIC_KEY
            else None
        )
        secret_key = (
            settings.LANGFUSE_SECRET_KEY.get_secret_value()
            if settings.LANGFUSE_SECRET_KEY
            else None
        )
        if public_key and secret_key:
            return Langfuse(public_key=public_key, secret_key=secret_key)
        return None
