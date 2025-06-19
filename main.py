from fastapi import FastAPI

from api import api, database

app = FastAPI()

app.include_router(api.router)


@app.on_event("startup")
async def startup_event():
    database.create_db_and_tables()
