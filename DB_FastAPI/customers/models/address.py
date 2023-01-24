from pydantic import BaseModel
from customers.models.account import Account
from customers.models.customer import Customer

class Address(BaseModel):
    id: int
    city: str
    state: str
    zip_code: str

    def __eq__(self, other):
        return self.id == other.id and self.city == other.city and \
            self.state == other.state and self.zip_code == other.zip_code