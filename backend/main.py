# backend/main.py

from fastapi import FastAPI
from backend.api import conflict

app = FastAPI()
app.include_router(conflict.router)
