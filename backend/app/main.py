from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.routes.hermes_routes import weight_router, run_router
from app.database import init_db
from fastapi.middleware.cors import CORSMiddleware


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield  # Tudo antes de yield acontece no startuo e tudo depois no shutdown


app = FastAPI(lifespan=lifespan)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Libera todas as origens
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


app.include_router(weight_router)
app.include_router(run_router)
