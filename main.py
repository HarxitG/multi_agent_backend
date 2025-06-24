from fastapi import FastAPI
from api.handlers import router

app = FastAPI()

# Register your routes
app.include_router(router)
