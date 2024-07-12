from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str
    PROJECT_VERSION: str
    DEBUG: bool
    DB_USER: str
    DB_PASSWORD: str
    DB_HOST: str
    DB_NAME: str

    class Config:
        env_file = ".env"

settings = Settings()