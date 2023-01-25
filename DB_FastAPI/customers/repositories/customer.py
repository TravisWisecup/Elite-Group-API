import psycopg2
from customers.models.customer import Customer

class CustomerRepository():
    db_name = 'customers.db'

    host = "localhost"
    database = "orders"
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
                    'FirstName': customer.customer_first,
                    'LastName': customer.customer_last,
                    'State': customer.customer_addressid,
                    'Email': customer.customer_email
                }
                )
                customer.id = cursor.fetchone()[0]
        return customer

    def get_by_id(self, id):
        with psycopg2.connect(host=self.host, database=self.database, user=self.user,
                              password=self.password) as db:
            with db.cursor() as cursor:
                cursor.execute("""
                    SELECT ID, FirstName, LastName, AddressID, Email FROM PRODUCT WHERE ID=%(id)s
                    """, {
                    'id': id
                }
                )
                row = cursor.fetchone()
                return Customer(id=row[0], FirstName=row[1], LastName=row[2], AddressId=row[3], Email=row[4])
