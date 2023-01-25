import psycopg2
from customers.models.address import Address

class AddressRepository():
    db_name = 'customers.db'

    connection = psycopg2.connect(
        host="localhost", #possibly change later!!
        database="psycopg",  #possibly change later!!
        user="postgres", #possibly change later!!
        password=None,
    )
    connection.set_session(autocommit=True)

    def insert(self, address: Address):
        with psycopg2.connect(host=self.host, database=self.database, user=self.user,
                              password=self.password) as db:
            with db.cursor() as cursor:
                cursor.execute("""
                    INSERT INTO ADDRESS
                        (ADDRESS_TEXT, ADDRESS_CITY, ADDRESS_STATE, ADDRESS_ZIPCODE) VALUES
                        (%(address_text)s, %(address_city)s, %(address_state)s, %(address_zipcode)s)
                        RETURNING ID
                    """, {
                    'address_text': address.address_text,
                    'address_city': address.address_city,
                    'address_state': address.address_state,
                    'address_zipcode': address.address_zipcode
                }
                )
                address.id = cursor.fetchone()[0]
        return address