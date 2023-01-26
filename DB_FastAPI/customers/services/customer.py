from customers.models.address import Address
from customers.models.customer import Customer
from customers.repositories.address import AddressRepository
from customers.repositories.customer import CustomerRepository

class CustomerService():
    def __init__(self, customer_repository: CustomerRepository, address_repository: AddressRepository):
        self.customer_repository = customer_repository
        self.address_repository = address_repository


    def add_new(self, customer: Customer):
        return self.customer_repository.insert(customer)