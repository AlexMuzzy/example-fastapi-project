import logging
from fastapi import APIRouter

router = APIRouter()
logger = logging.getLogger(__name__)


@router.get("")
async def get_birute():
    return {"name": "Birute"}
