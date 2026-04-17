from pydantic import BaseModel , Field
from typing import Optional , List



class Item(BaseModel):
    name: str
    description: Optional[str] = Field( ... , description="The description of the item")
    price: float = Field( ... , description="The price of the item")
    tax: Optional[float] = Field( ... , description="The tax rate for the item")
    count: List[int] = Field( ... , description="The count of the item in stock")


class ItemResponse(BaseModel):
    name: str
    final_price: float
    
    
    