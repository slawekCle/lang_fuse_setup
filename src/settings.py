from pydantic import SecretStr, AnyUrl
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    LITELLM_MASTER_KEY: SecretStr = None
    LITELLM_URL: str = None

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
        env_file_encoding="utf-8"
    )
