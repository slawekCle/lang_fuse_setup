import pprint
import sys

from openai import OpenAI

from src.lite_prompter import LitePrompter
from src.prompter import Prompter
from src.settings import Settings

if __name__ == "__main__":
    settings = Settings()

    prompter = Prompter(settings.LITELLM_URL, settings.LITELLM_MASTER_KEY.get_secret_value())
    # prompter = LitePrompter(settings.LITELLM_URL, settings.LITELLM_MASTER_KEY.get_secret_value())
    pprint.pprint(prompter.run(sys.argv[1]))
