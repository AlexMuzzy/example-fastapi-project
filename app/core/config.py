from pydantic_settings import BaseSettings
from os import environ


class Settings(BaseSettings):
    PROJECT_NAME: str = "Example FastAPI Project"
    PROJECT_VERSION: str = "0.1.0 (dev)"
    DEBUG: bool = False
    DB_USER: str
    DB_PASSWORD: str
    DB_HOST: str
    DB_NAME: str

    class Config:
        env_file = ".env"


settings = Settings()
