from pydantic import BaseModel , Field
from typing import Optional , List


class User(BaseModel):
    user_name : str = Field(..., description="The name of the user" )
    user_email : Optional[str] = Field(None, description="The email of the user" )
    post : List[str] = Field(...,description="The Post desc is required")



