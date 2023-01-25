from pydantic import BaseModel
from customers.models.customer import Customer

class Account(BaseModel):
    id: int
    account_num: str
    customer: Customer
    current_balance: float