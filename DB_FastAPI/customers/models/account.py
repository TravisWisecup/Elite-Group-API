from pydantic import BaseModel
from customers.models.address import Address
from customers.models.customer import Customer

class Account(BaseModel):
    id: int
    account_num: str
    customer_id: int
    current_balance: float

    def __eq__(self, other):
        return self.id == other.id and self.account_num == other.account_num and \
            self.customer_id == other.customer_id and self.current_balance == other.current_balance