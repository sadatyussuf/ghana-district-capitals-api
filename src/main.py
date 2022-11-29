from fastapi import FastAPI

from .database import connect_to_database
from .routes import district_capitals

connect_to_database()
app = FastAPI()

app.include_router(district_capitals.router)
# connect to database


@app.get("/")
def home():
    return {"Welcome to Ghana Districts API"}
