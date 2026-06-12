"""Configuration for the application"""
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    """Configuration for the application"""
    model_config = SettingsConfigDict(env_file=".env")

    DATABASE_URL: str
    GOOGLE_GENAI_API_KEY: str
    GOOGLE_GENAI_MODEL: str
    JWT_SECRET_KEY:str

settings = Settings()
