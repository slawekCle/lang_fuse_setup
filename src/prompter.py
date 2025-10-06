import pprint

from openai import OpenAI
from openai.types.chat import ChatCompletion


class Prompter:

    def __init__(self, base_url:str, api_key: str):
        self.base_url = base_url
        self.api_key = api_key
        self.client = OpenAI(base_url=base_url, api_key=api_key)

    def run(self, prompt: str) -> None:
        """ run prompt"""

        completion = self.client.chat.completions.create(
            model="main",
            messages=[{"role": "user", "content": prompt}],
            temperature=1,
            max_tokens=8192,
            stream=False,
            stop=None,
        )
        return self._extract_completion_content(completion)

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
