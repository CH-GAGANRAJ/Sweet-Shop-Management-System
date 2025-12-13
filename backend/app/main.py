from fastapi import FastAPI
from app import auth_routes, auth, sweets_routes, models, db

# Create database tables
models.Base.metadata.create_all(bind=db.engine)

app = FastAPI()
app.include_router(auth_routes.router)
app.include_router(sweets_routes.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Sweet Shop API"}