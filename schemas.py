from pydantic import BaseModel, Field, EmailStr
from typing import List
class Email(BaseModel):
    header : str = Field(..., min_length=1, max_length=30)
    body : str = Field(..., min_length=1)
    recipients : List[EmailStr]

class EmailResponse(BaseModel):
    status : str
    detail : str = ''
