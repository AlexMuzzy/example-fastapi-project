from app.core.db import SessionLocal
from app.models.item import Item, ItemDB, ItemCreate


class ItemService:
    def __init__(self):
        self.db = SessionLocal()

    def get_item(self, item_id: int) -> Item | None:
        return self.db.query(ItemDB).filter(Item.id == item_id).first()

    def create_item(self, item: ItemCreate) -> Item:
        new_id = self.db.query(ItemDB).count() + 1
        new_item = ItemDB(id=new_id, name=item.name, description=item.description)
        self.db.add(new_item)
        self.db.commit()
        return new_item

    def list_items(self, skip: int = 0, limit: int = 10) -> list[Item]:
        return list(self.db.query(ItemDB).all())[skip : skip + limit]
