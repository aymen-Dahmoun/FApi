
from app.core.database import Base
from pydantic import EmailStr

class User(Base):
    email: EmailStr
    hashed_password: str

    class Settings:
        name = "users"
