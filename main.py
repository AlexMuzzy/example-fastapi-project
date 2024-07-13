from os import environ
from sys import path
from fastapi import FastAPI

from app.core.config import settings
from app.api.items import router as item_router
from app.api.birute import router as birute_router
from app.core.db import Base, engine
from app.core.logging import configure_logging

app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)

app.include_router(item_router, prefix="/items", tags=["items"])
app.include_router(birute_router, prefix="/birute", tags=["birute"])

configure_logging()

Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    import uvicorn

    if environ.get("ENV") == "production":
        path.append(path.dirname(path.dirname(__file__)))

    uvicorn.run(app)
