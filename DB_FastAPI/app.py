import uvicorn
from fastapi import FastAPI
from customers.repositories.account import AccountRepository
from customers.repositories.customer import CustomerRepository
from customers.repositories.address import AddressRepository
from customers.models.address import Address
from customers.models.account import Account
from customers.models.customer import Customer
from customers.services.account import AccountService
from customers.services.customer import CustomerService
from customers.services.address import AddressService
from typing import List

app = FastAPI()
address_repository = AddressRepository()
customer_repository = CustomerRepository()
account_repository = AccountRepository()
account_service = AccountService(account_repository, address_repository, customer_repository)
customer_service = CustomerService(customer_repository, address_repository)
address_service = AddressService(address_repository)


@app.get('/api/accounts', response_model=List[Account])
async def retrieve_accounts():
    return account_service.get_all()


@app.get('/api/accounts/{account_number}')
async def retrieve_product_by_number(account_number):
    account = account_service.get_one(account_number)
    if account:
        return account
    else:
        return {}


@app.post('/api/acounts/new')
async def create_account(account: Account):
    return account_service.add_new(account)

@app.post('/api/address/new')
async def create_address(address: Address):
    return address_service.add_new(address)

@app.post('/api/customer/new')
async def create_customer(customer: Customer):
    return customer_service.add_new(customer)

# @app.put('/api/products/{id}')
# async def update_product(id, product: Product):
#     product.id = id
#     return product_service.update(product)


# @app.post('/api/orders/new')
# async def create_order(order: Order):
#     return order_service.add_new(order)


# @app.get('/api/orders/{order_number}')
# async def retrieve_order_by_number(order_number):
#     order = order_service.get_one(order_number)
#     if order:
#         return order
#     else:
#         return {}

if __name__ == "__main__":
     uvicorn.run("app:app", host="0.0.0.0", port=8080, reload=True,
                 timeout_keep_alive=3600, workers=10)