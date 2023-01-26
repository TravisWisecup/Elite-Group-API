import unittest
from customers.models.account import Account
from customers.models.address import Address
from customers.models.customer import Customer
from customers.repositories.account import Account
from customers.repositories.address import Address
from customers.repositories.customer import Customer


class TestAccountRepository(unittest.TestCase):
    def setUp(self):
        self.accountRepository = Account()
        self.addressRepository = Address()
        self.customerRepository = Customer()
        self.inserted_address = self.Address.insert(
            Address(id=0, address_text="123 BLVD", address_city="Los Angeles", address_state = "CA", address_zicode = "12345"))
        self.inserted_customer = \
            self.Customer.insert(Customer(
                id=0, customer_first="Chris", customer_last="Yin", customer_addressid=0, customer_email="chrisiscool@gmail.com"))
        self.inserted_account = \
            self.Account.insert(Account(
                id=0, account_num="10101010", customer_id=0, current_balance=1000000.10
            )) 

    def tearDown(self):
        self.Account.delete(self.inserted_account.id)

    def test_get_by_number(self):
        get_order = self.Account.get_by_num(
            self.inserted_account.address_text)
        self.inserted_account.address = Product(id=self.inserted_product.id, product_number='', description='', unit_cost=0.0)
        self.assertEqual(get_order, self.inserted_order)


if __name__ == "__main__":
    unittest.main()