from fastapi import APIRouter, HTTPException, Depends
from app.models.item import Item, ItemCreate
from app.services.item_service import ItemService
import logging

router = APIRouter()
logger = logging.getLogger(__name__)

@router.get("/items/{item_id}", response_model=Item)
async def get_item(item_id: int, service: ItemService = Depends()):
    item = service.get_item(item_id)
    if item is None:
        logger.warning(f"Item with id {item_id} not found")
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@router.post("/items", response_model=Item, status_code=201)
async def create_item(item: ItemCreate, service: ItemService = Depends()):
    return service.create_item(item)

@router.get("/items", response_model=list[Item])
async def list_items(skip: int = 0, limit: int = 10, service: ItemService = Depends()):
    return service.list_items(skip, limit)