import unittest
from unittest.mock import Mock
from customers.models.account import Account
from customers.models.address  import Address
from customers.models.customer import Customer

from customers.repositories.account import Account
from customers.repositories.address  import Address
from customers.repositories.customer import Customer


class TestOrderService(unittest.TestCase):
    def setUp(self):
        self.accountRepository = Account()
        self.addressRepository = Address()
        self.customerRepository = Customer()

        self.customer = Customer (id=1, firstname="John", lastname='Doe', address_id =1, email = "garbageman@gmail.com")
        self.address = Address(id=1, address="pizza street", city="chilltown", state="CA", zip_code=12345)
        self.account = Account(id=1, account_num =123,
                          customer_id= 1, current_balance= 50.00)

        #self. = (id=1, order_number="456",
         #                  product=self.product, quantity=1, total=1.00)
        self.customer_repo = Mock()
        self.address_repo = Mock()
        self.account_repo = Account(self.account, self.customer, self.address)

    def test_add_new(self):
        self.account.get_by_num = Mock(return_value=self.account)
        self.address.insert = Mock(return_value=self.address)
        self.customer.insert = Mock (return_value= self.customer)
        new_account = self.account.add_new(self.account)
        self.assertEqual(new_account, self.order)

    def test_get_by_num(self):
        self.orderRepository.get_by_number = Mock(return_value=self.order)
        get_order = self.orderService.get_one("000")
        self.assertEqual(get_order, self.order)
    
    def test_withdraw(self):
    
    def test_deposit(self):

    def get_all(self):


if __name__ == "__main__":
    unittest.main()