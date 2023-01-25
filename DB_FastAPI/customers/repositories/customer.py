import psycopg2
from customers.models.customer import Customer

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
        with psycopg2.connect(host=self.host, database=self.database, user=self.user,
                              password=self.password) as db:
            with db.cursor() as cursor:
                cursor.execute("""
                    INSERT INTO CUSTOMER
                        (CUSTOMER_FIRST, CUSTOMER_LAST, CUSTOMER_ADDRESSID, CUSTOMER_EMAIL) VALUES
                        (%(customer_first)s, %(customer_last)s, %(customer_addressid)s, %(customer_email)s)
                        RETURNING ID
                    """, {
                    'customer_first': customer.customer_first,
                    'customer_last': customer.customer_last,
                    'customer_addressid': customer.customer_addressid,
                    'customer_email': customer.customer_email
                }
                )
                customer.id = cursor.fetchone()[0]
        return customer