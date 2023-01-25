from pydantic import BaseModel
from customers.models.address import Address

class Customer(BaseModel):
    id: int
    first_name: str
    last_name: str
    address_id: Address
    email: str