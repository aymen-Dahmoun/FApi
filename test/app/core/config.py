import os
from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    APP_NAME: str = "test"

    DATABASE_URL: str = os.getenv("DATABASE_URL", "mongodb://localhost:27017")



    SECRET_KEY: str = os.getenv("SECRET_KEY", "supersecretkey")
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30



    class Config:
        env_file = ".env"
        extra = "allow"

settings = Settings()

# Explicitly export mapped settings for cleaner imports
APP_NAME = settings.APP_NAME

DATABASE_URL = settings.DATABASE_URL



SECRET_KEY = settings.SECRET_KEY
ALGORITHM = settings.ALGORITHM
ACCESS_TOKEN_EXPIRE_MINUTES = settings.ACCESS_TOKEN_EXPIRE_MINUTES

