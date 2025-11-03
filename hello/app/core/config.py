from pydantic import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "hello"

    DATABASE_URL: str = "sqlite:///./app.db"


    class Config:
        env_file = ".env"

settings = Settings()