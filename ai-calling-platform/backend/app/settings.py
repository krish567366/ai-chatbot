from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import List


class Settings(BaseSettings):
	APP_ENV: str = "dev"
	SECRET_KEY: str
	DATABASE_URL: str
	REDIS_URL: str
	S3_ENDPOINT: str
	S3_ACCESS_KEY: str
	S3_SECRET_KEY: str
	S3_BUCKET: str
	OPENAI_API_KEY: str | None = None
	AZURE_TTS_KEY: str | None = None
	TWILIO_ACCOUNT_SID: str | None = None
	TWILIO_AUTH_TOKEN: str | None = None
	PUBLIC_BASE_URL: str
	RATE_LIMIT_DEFAULT_RPS: int = 10
	FEATURE_FLAGS: List[str] = []

	model_config = SettingsConfigDict(env_file=".env.dev", env_file_encoding="utf-8")


settings = Settings()