
from fastapi import FastAPI

from app.api.routes.auth import router as auth_router

app = FastAPI(
    title="AuthForge API",
    description="A production-oriented authentication and authorization service.",
    version="1.0.0",
)


@app.get("/", tags=["Health"])
def root():
    return {
        "message": "Welcome to AuthForge API",
        "status": "running",
    }


@app.get("/health", tags=["Health"])
def health_check():
    return {"status": "healthy"}


@app.get("/api/v1/info", tags=["Information"])
def get_api_info():
    return {
        "project": "AuthForge",
        "version": "1.0.0",
        "description": "Authentication and authorization API",
    }


app.include_router(
    auth_router,
    prefix="/api/v1/auth",
    tags=["Authentication"],
)
