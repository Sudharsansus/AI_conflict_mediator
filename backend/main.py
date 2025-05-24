from fastapi import FastAPI
from backend.api import conflict
from backend.api import admin  # 👈 Add this

app = FastAPI()

app.include_router(conflict.router)
app.include_router(admin.router, prefix="/admin")  # 👈 Add this
