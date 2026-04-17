from fastapi import APIRouter
from models.items_model import Item, ItemResponse
from controllers.item_controller import create_item


router = APIRouter()


@router.post("/items/", response_model=ItemResponse())
def add_item(item: Item):
    return create_item(item)


