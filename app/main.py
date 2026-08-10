from fastapi import FastAPI

from app.api.v1.api import api_router
from app.core.config import settings
from app.db.session import init_db

app = FastAPI()

app.include_router(api_router, prefix="/api/v1")

@app.on_event("startup")
def on_startup():
    init_db()

@app.get("/")
def root ():
    return {"message":"Hello"}

@app.get("/api/health")
def health_check():
    return {"status":"ok"}