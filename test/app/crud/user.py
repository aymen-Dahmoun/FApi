
from app.models.user import User
from app.schemas.user import UserCreate
import bcrypt

async def create_user(user: UserCreate):
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(user.password.encode('utf-8'), salt).decode('utf-8')
    db_user = User(email=user.email, hashed_password=hashed)
    await db_user.insert()
    return db_user

async def get_users():
    return await User.find_all().to_list()
