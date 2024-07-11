from db import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel

# SQLAlchemy model
class ItemDB(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, nullable=True)

# Pydantic models
class ItemBase(BaseModel):
    name: str
    description: str | None = None

class ItemCreate(ItemBase):
    pass

class Item(ItemBase):
    id: int

    class Config:
        orm_mode = True

# Conversion functions
def to_pydantic(db_model: ItemDB) -> Item:
    return Item.from_orm(db_model)

def to_sqlalchemy(pydantic_model: ItemCreate) -> ItemDB:
    return ItemDB(**pydantic_model.dict())