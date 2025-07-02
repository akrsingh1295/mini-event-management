from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.api.endpoints import router
from app.core.database import init_db

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup logic here
    await init_db()
    yield
    # Shutdown logic (if needed)

app = FastAPI(lifespan=lifespan)

app.include_router(router)
