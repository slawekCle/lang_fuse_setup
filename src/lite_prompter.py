
from litellm import completion

class LitePrompter:

    def __init__(self, base_url: str, api_key: str):
        self.base_url = base_url
        self.api_key = api_key

    def run(self, prompt: str) -> str:
        print(self.base_url)
        output = completion(
            model="main",
            messages=[{"role": "user", "content": prompt}],
            temperature=1,
            api_key=self.api_key,
            base_url=self.base_url,
            custom_llm_provider="openai"
        )

        return output["choices"][0]["message"]["content"]