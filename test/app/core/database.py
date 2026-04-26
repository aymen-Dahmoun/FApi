
from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie, Document
from app.core.config import DATABASE_URL

client = AsyncIOMotorClient(DATABASE_URL)
Base = Document

async def init_db():
    await init_beanie(database=client.app_db, document_models=[])

async def get_db():
    yield client.app_db



