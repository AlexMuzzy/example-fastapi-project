from os import environ, path
from sys import path
from fastapi import FastAPI
from api.items import router as item_router
from api.birute import router as birute_router
from core.config import settings
from core.db import Base, engine
from core.logging import configure_logging

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
