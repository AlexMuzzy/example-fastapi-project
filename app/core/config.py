from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "FastAPI Project"
    PROJECT_VERSION: str = "1.0.0"
    DEBUG: bool = False

    class Config:
        env_file = ".env"

settings = Settings()