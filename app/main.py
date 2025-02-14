from contextlib import asynccontextmanager
from typing import Union

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from sqlmodel import SQLModel

from app.routers import common, user
from app.database import engine


@asynccontextmanager
async def lifespan(_: FastAPI):
    SQLModel.metadata.create_all(engine)
    yield


app = FastAPI(lifespan=lifespan)


app.include_router(common.router)
app.include_router(user.router)


@app.get("/")
def read_root():
    return "Hello, World!"
