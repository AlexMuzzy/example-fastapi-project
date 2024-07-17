from pydantic_settings import BaseSettings
from os import environ


class Settings(BaseSettings):
    PROJECT_NAME: str = "Example FastAPI Project"
    PROJECT_VERSION: str = "0.1.0 (dev)"
    DEBUG: bool = False
    DB_USER: str = "postgres"
    DB_PASSWORD: str = "#KQrwQi8az4j.D9"
    DB_HOST: str = "db.nbkaacxetceifqkzbgkf.supabase.co:5432"
    DB_NAME: str = "postgres"

    class Config:
        env_file = ".env.production" if environ.get("ENV") == "production" else ".env"


settings = Settings()
