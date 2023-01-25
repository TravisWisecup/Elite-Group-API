import psycopg2
from customers.models.customer import Customer
from customers.models.address import Address

class CustomerRepository():
    db_name = 'customers.db'

    host = "localhost"
    database = "psycopgtest"
    user = "postgres"
    password = "password123"

    def insert(self, customer: Customer):
        with psycopg2.connect(host=self.host, database=self.database, user=self.user,
                              password=self.password) as db:
            with db.cursor() as cursor:
                cursor.execute("""
                    INSERT INTO customer
                        (FirstName, LastName, State, AddressID, Email) VALUES
                        (%(customer_first)s, %(customer_last)s, %(customer_addressid)s, %(customer_email)s)
                        RETURNING ID
                    """, {
                    'customer_first': customer.first_name,
                    'customer_last': customer.last_name,
                    'customer_addressid': customer.address,
                    'customer_email': customer.email
                }
                )
                customer.id = cursor.fetchone()[0]
        return customer

    def get_by_id(self, id):
        with psycopg2.connect(host=self.host, database=self.database, user=self.user,
                              password=self.password) as db:
            with db.cursor() as cursor:
                cursor.execute("""
                    SELECT ID, FirstName, LastName, AddressID, Email FROM customer WHERE ID=%(id)s
                    """, {
                    'id': id
                }
                )
                row = cursor.fetchone()
                if row:
                    address = Address(id=row[3], address='', city='', state='', zip_code='')
                    return Customer(id=row[0], first_name=row[1], last_name=row[2], address=address, email=row[4])
                else:
                    return None
