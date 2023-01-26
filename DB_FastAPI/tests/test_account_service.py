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
        self.accountRepository = Account();
        self.addressRepository = Address();
        self.customerRepository = Customer();

        self.customer = Customer(id=1, firstname="John", lastname='Doe'
                          description="desc", unit_cost=1.00)
        self.address = Address(id=1, address="pizza street", city="chilltown", state="CA", zip_code=12345)
        self.account = Account(id=1, account_num =123,
                          customer_id= 1, current_balance= 50.00)
    

        

        #self. = (id=1, order_number="456",
         #                  product=self.product, quantity=1, total=1.00)
        self.product_repository = Mock()
        self.orderRepository = Mock()
        self.customerRepository = Customer(self.orderRepository, self.product_repository)

    def test_add_new(self):
        self.product_repository.get_by_id = Mock(return_value=self.product)
        self.orderRepository.insert = Mock(return_value=self.order)
        new_order = self.orderService.add_new(self.order)
        self.assertEqual(new_order, self.order)

    def test_get_by_num(self):
        self.orderRepository.get_by_number = Mock(return_value=self.order)
        get_order = self.orderService.get_one("000")
        self.assertEqual(get_order, self.order)
    
    def test_withdraw(self):
    
    def test_deposit(self):

    def get_all(self):


if __name__ == "__main__":
    unittest.main()