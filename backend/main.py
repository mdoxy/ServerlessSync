from fastapi import FastAPI
from app.routes.upload import router as upload_router

app = FastAPI(title="ServerlessSync")

app.include_router(upload_router)

@app.get("/")
def home():
    return {"message": "ServerlessSync Running"}
