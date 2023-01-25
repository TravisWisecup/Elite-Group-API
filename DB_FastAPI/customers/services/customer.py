from customers.models.address import Address
from customers.models.customer import Customer
from customers.repositories.address import AddressRepository
from customers.repositories.customer import CustomerRepository

class CustomerService():
    def __init__(self, address_repository: AddressRepository, customer_repository: CustomerRepository):
        self.address_respository = address_repository
        self.customer_respository = customer_repository

    def add_new(self, customer: Customer, address: Address):
        address = self.address_respository.get_by_id(customer.address.id)
        customer.address = address
        return self.customer_repository.insert(customer)