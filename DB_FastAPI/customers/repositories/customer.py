import psycopg2
from customers.models.account import Account
from customers.models.customer import Customer
from customers.models.address import Address

class CustomerRepository():
    db_name = 'customers.db'

    connection = psycopg2.connect(
        host="localhost", #possibly change later!!
        database="psycopgtest",  #possibly change later!!
        user="postgres", #possibly change later!!
        password=None,
    )
    connection.set_session(autocommit=True)

    def insert(self, customer: Customer):
        with cursor.connect() as cursor:
            cursor.execute('INSERT INTO [customer] (FirstName, LastName, AddressID, Email) VALUES \
                (?, ?, ?, ?)', [customer.first_name, customer.last_name, customer.address_id, customer.email])
        customer.id = cursor.lastrowid
        return customer