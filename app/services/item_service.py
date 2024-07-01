from app.models.item import Item, ItemCreate

class ItemService:
    def __init__(self):
        self.items = {}

    def get_item(self, item_id: int) -> Item | None:
        return self.items.get(item_id)

    def create_item(self, item: ItemCreate) -> Item:
        item_id = len(self.items) + 1
        new_item = Item(id=item_id, **item.dict())
        self.items[item_id] = new_item
        return new_item

    def list_items(self, skip: int = 0, limit: int = 10) -> list[Item]:
        return list(self.items.values())[skip : skip + limit]