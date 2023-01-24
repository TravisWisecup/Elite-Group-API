import psycopg2
from customers.models.account import Account
from customers.models.customer import Customer
from customers.models.address import Address

class AddressRepository():
    db_name = 'customers.db'

    connection = psycopg2.connect(
        host="localhost", #possibly change later!!
        database="psycopgtest",  #possibly change later!!
        user="postgres", #possibly change later!!
        password=None,
    )
    connection.set_session(autocommit=True)

    def insert(self, address: Address):
        with cursor.connect() as cursor:
            cursor.execute('INSERT INTO [address] (Address, City, State, ZipCode) VALUES \
                (?, ?, ?, ?)', [address.address, address.city, address.state, address.zip_code])
        address.id = cursor.lastrowid
        return address