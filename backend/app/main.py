from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.routes.hermes_routes import router
from app.database import init_db


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield  # Tudo antes de yield acontece no startuo e tudo depois no shutdown


app = FastAPI(lifespan=lifespan)

app.include_router(router)
