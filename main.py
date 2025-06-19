import uvicorn
from fastapi import FastAPI

from api import api, database

app = FastAPI()

app.include_router(api.router)


@app.on_event("startup")
async def startup_event():
    database.create_db_and_tables()

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
