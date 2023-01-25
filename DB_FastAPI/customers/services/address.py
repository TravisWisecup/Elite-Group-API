from customers.models.address import Address
from customers.models.customer import Customer
from customers.repositories.address import AddressRepository
from customers.repositories.customer import CustomerRepository

class AddressService():
    def __init__(self, address_repository: AddressRepository, customer_repository: CustomerRepository):
        self.address_respository = address_repository
        self.customer_respository = customer_repository

    def add_new(self, customer: Customer, address: Address):
        customer = self.customer_respository.get_by_id(address.customer.id)
        address.customer = customer
        return self.address_repository.insert(address)