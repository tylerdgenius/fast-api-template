# app/server.py
from fastapi import FastAPI
from config.env import Environment
from config.deps import db

env = Environment()

def create_app() -> FastAPI:
    app = FastAPI(
        title="FastAPI Template",
        description="A template for FastAPI applications",
        version="1.0.0",
    )

    # --- middleware / CORS / routers go here ---
    # from .routers import users
    # app.include_router(users.router, prefix="/api")

    @app.get("/health", tags=["health"])
    def health():
        return {"ok": True}

    @app.on_event("startup")
    def on_startup():
        if not db.ping():
            raise RuntimeError("PostgreSQL not reachable")
        print("App starting up…")

    @app.on_event("shutdown")
    def on_shutdown():
        print("App shutting down…")

    return app

app = create_app()  # uvicorn entrypoint uses this