from customers.models.account import Account
from customers.models.address import Address
from customers.models.customer import Customer
from customers.repositories.account import AccountRepository
from customers.repositories.address import AddressRepository
from customers.repositories.customer import CustomerRepository

class AccountService():
    def __init__(self, account_repository: AccountRepository, address_repository: AddressRepository, customer_repository: CustomerRepository):
        self.account_repository = account_repository
        self.address_respository = address_repository
        self.customer_respository = customer_repository

    def add_new(self, account: Account):
        return self.account_repository.insert(account)

    def get_by_num(self, account_number):
        account = self.account_repository.get_by_num(account_number)
        customer = self.customer_respository.get_by_id(account.customer.id)
        address = self.address_respository.get_by_id(customer.address.id)
        customer.address = address
        account.customer = customer
        return account

    def withdraw(self, withdrawal_amount):
        account = self.account_repository.deposit(withdrawal_amount)
        return account

    def deposit(self, deposit_amount):
        account = self.account_repository.deposit(deposit_amount)
        return account

    def get_all(self):
        return self.account_repository.get_all_accounts()