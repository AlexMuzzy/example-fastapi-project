from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "Example FastAPI Project"
    PROJECT_VERSION: str = "0.1.0 (dev)"
    DEBUG: bool = False

    class Config:
        env_file = ".env"

settings = Settings()