"""Application configuration loaded from environment variables."""

from functools import lru_cache
from typing import List

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )

    APP_NAME: str = "real-estate-lead-bot"
    APP_ENV: str = "development"
    APP_DEBUG: bool = True
    APP_HOST: str = "0.0.0.0"
    APP_PORT: int = 8000

    DATABASE_URL: str = "postgresql://postgres:postgres@localhost:5432/real_estate_leads"

    JWT_SECRET: str = "change-me"
    JWT_ALGORITHM: str = "HS256"
    JWT_EXPIRE_MINUTES: int = 1440

    CORS_ORIGINS: List[str] = ["http://localhost:3000", "http://localhost:5173"]

    N8N_WEBHOOK_URL: str = "http://localhost:5678/webhook"
    N8N_WEBHOOK_SECRET: str = ""

    AI_API_KEY: str = ""
    AI_MODEL: str = "gpt-4o-mini"
    AI_TIMEOUT_SECONDS: int = 30


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
