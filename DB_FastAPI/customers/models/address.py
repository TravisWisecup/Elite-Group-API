from pydantic import BaseModel
from customers.models.account import Account
from customers.models.customer import Customer

class Address(BaseModel):
    id: int
    address: str
    city: str
    state: str
    zip_code: str

    def __eq__(self, other):
        return self.id == other.id and self.city == other.city and \
            self.address == other.address and \
            self.state == other.state and self.zip_code == other.zip_code