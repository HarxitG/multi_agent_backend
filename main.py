from fastapi import FastAPI
from api.handlers import router

app = FastAPI()
app.include_router(router)

@app.get("/")  # <-- Add this
def root():
    return {"message": "API is running"}
