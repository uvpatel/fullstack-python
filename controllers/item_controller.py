from models.items_model import Item, ItemResponse


def create_item(item: Item) -> ItemResponse:
    final_price = item.price * (1 + (item.tax or 0))
    return ItemResponse(name=item.name, final_price=final_price)
