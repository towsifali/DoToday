from fastapi import FastAPI
from src.core.config import settings
from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
)


@app.on_event("startup")
async def app_init():
    """
        Initialize the app
    """

    db_client = AsyncIOMotorClient(settings.MONGO_CONNECTION_STRING).todolist

    await init_beanie(database=db_client, document_models=[

    ])
