from fastapi import FastAPI

from src.impl.database import database


app = FastAPI()

@app.on_event("startup")  # type: ignore
async def startup() -> None:
    await database.connect()
