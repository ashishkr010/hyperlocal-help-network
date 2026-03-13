from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from loguru import logger
import sys

from app.middleware.middleware import RequestMiddleware
from app.routers import auth, users, requests, offers, reviews

logger.remove()
logger.add(sys.stdout, level="INFO")
logger.add("logs/app.log", rotation="10 MB", serialize=True)

app = FastAPI(title="Hyperlocal Help Network")

app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])
app.add_middleware(RequestMiddleware)

app.include_router(auth.router)
app.include_router(users.router)
app.include_router(requests.router)
app.include_router(offers.router)
app.include_router(reviews.router)


@app.get("/")
async def root():
    return {"message": "Hyperlocal Help Network API"}
