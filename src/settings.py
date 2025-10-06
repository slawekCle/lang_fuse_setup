from pydantic import SecretStr, AnyUrl
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    LITELLM_MASTER_KEY: SecretStr | None = None
    LITELLM_URL: str | None = None
    LANGFUSE_PUBLIC_KEY: SecretStr | None = None
    LANGFUSE_SECRET_KEY: SecretStr | None = None
    LANGFUSE_HOST: str | None = None


    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
        env_file_encoding="utf-8"
    )
