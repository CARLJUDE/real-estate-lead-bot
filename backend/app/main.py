"""
FastAPI application entrypoint.

PrimeHomes Realty — Real Estate Lead Bot
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings
from app.api.v1.health import router as health_router

app = FastAPI(
    title=settings.APP_NAME,
    version="0.1.0",
    description="AI-powered real estate lead management system for PrimeHomes Realty",
    docs_url="/docs",
    redoc_url="/redoc",
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# API routers
app.include_router(health_router, prefix="/api/v1", tags=["health"])

# Future routers (to be added in subsequent phases):
# app.include_router(auth_router, prefix="/api/v1/auth", tags=["auth"])
# app.include_router(leads_router, prefix="/api/v1/leads", tags=["leads"])
# app.include_router(conversations_router, prefix="/api/v1/conversations", tags=["conversations"])
# app.include_router(messages_router, prefix="/api/v1/messages", tags=["messages"])
# app.include_router(followups_router, prefix="/api/v1/follow-ups", tags=["follow-ups"])


@app.get("/")
def root():
    return {
        "service": settings.APP_NAME,
        "status": "ok",
        "docs": "/docs",
    }
