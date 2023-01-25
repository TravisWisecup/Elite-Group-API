import psycopg2
from customers.models.address import Address

class AddressRepository():
    db_name = 'customers.db'

    host = "localhost"
    database = "psycopgtest"
    user = "postgres"
    password = "password123"

    def insert(self, address: Address):
        with psycopg2.connect(host=self.host, database=self.database, user=self.user,
                              password=self.password) as db:
            with db.cursor() as cursor:
                cursor.execute("""
                    INSERT INTO address
                        (Address, City, State, ZipCode) VALUES
                        (%(address_text)s, %(address_city)s, %(address_state)s, %(address_zipcode)s)
                        RETURNING ID
                    """, {
                    'address_text': address.address,
                    'address_city': address.city,
                    'address_state': address.state,
                    'address_zipcode': address.zip_code
                }
                )
                address.id = cursor.fetchone()[0]
        return address

    def get_by_id(self, id):
        with psycopg2.connect(host=self.host, database=self.database, user=self.user,
                              password=self.password) as db:
            with db.cursor() as cursor:
                cursor.execute("""
                    SELECT ID, Address, City, State, ZipCode FROM address WHERE ID=%(id)s
                    """, {
                    'id': id
                }
                )
                row = cursor.fetchone()
                return Address(id=row[0], address=row[1], city=row[2], state=row[3], zipcode=row[4])