from fastapi import APIRouter, HTTPException, Depends
from models.item import Item, ItemCreate
from services.item_service import ItemService
import logging

router = APIRouter()
logger = logging.getLogger(__name__)

@router.get("/{item_id}", response_model=Item)
async def get_item(item_id: int, item_service: ItemService = Depends()):
    item = item_service.get_item(item_id)
    if item is None:
        logger.warning(f"Item with id {item_id} not found")
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@router.post("", response_model=Item, status_code=201)
async def create_item(item: ItemCreate, item_service: ItemService = Depends()):
    return item_service.create_item(item)

@router.get("", response_model=list[Item])
async def list_items(skip: int = 0, limit: int = 10, item_service: ItemService = Depends()):
    return item_service.list_items(skip, limit)