from pydantic import BaseModel
from customers.models.account import Account

class Address(BaseModel):
    id: int
    address: str
    city: str
    state: str
    zip_code: str