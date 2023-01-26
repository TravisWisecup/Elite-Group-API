from customers.models.address import Address
from customers.repositories.address import AddressRepository

class AddressService():
    def __init__(self, address_repository: AddressRepository):
        self.address_repository = address_repository

    def add_new(self, address: Address):
        return self.address_repository.insert(address)
