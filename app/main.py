from db import Base, engine
from fastapi import FastAPI
from api.items import router as item_router
from api.birute import router as birute_router
from core.config import settings
from core.logging import configure_logging

app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)

app.include_router(item_router, prefix="/items", tags=["items"])
app.include_router(birute_router, prefix="/birute", tags=["birute"])

configure_logging()

Base.metadata.create_all(bind=engine)

@app.on_event("startup")
async def startup_event():
    print(f"Starting up {settings.PROJECT_NAME}")

@app.on_event("shutdown")
async def shutdown_event():
    print(f"Shutting down {settings.PROJECT_NAME}")

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app)