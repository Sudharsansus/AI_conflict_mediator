from fastapi import FastAPI
from backend.api import conflict  # or wherever the router is

app = FastAPI()

app.include_router(conflict.router, prefix="/")  # ✅ Make sure this line exists

# Also include CORS if needed
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can replace '*' with your frontend URL in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
