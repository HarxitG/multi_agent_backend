from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from api.handlers import router

app = FastAPI()

# Include your API routes
app.include_router(router)

# Root route redirects to Swagger docs
@app.get("/")
def root():
    return RedirectResponse(url="/docs")
