from fastapi import FastAPI
from app.database.database import Base, engine
from app.models.user import User
from app.api.users import router as users_router
from app.models.url import URL
from app.api.urls import router as urls_router

app = FastAPI(title="URLX API")

Base.metadata.create_all(bind=engine)

app.include_router(users_router)
app.include_router(urls_router)

@app.get("/")
def home():
    return {"message": "URLX API is running"}