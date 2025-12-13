from fastapi import FastAPI
from app import auth_routes, auth

app = FastAPI()
app.include_router(auth_routes.router)
