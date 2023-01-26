import psycopg2
from customers.models.account import Account
from customers.models.customer import Customer
from customers.models.address import Address
from customers.services.customer import CustomerService

class AccountRepository():
    host = "localhost"
    database = "psycopgtest"
    user = "postgres"
    password = "password123"

    def insert(self, account: Account):
        with psycopg2.connect(host=self.host, database=self.database, user=self.user,
                            password=self.password) as db:
            with db.cursor() as cursor:
                cursor.execute("""
                INSERT INTO account
                (AccountNum, CustomerID, CurrentBalance) VALUES
                (%(account_num)s, %(customer_id)s, %(current_balance)s)
                RETURNING ID
                """, {
                    'account_num': account.account_num,
                    'customer_id': account.customer.id,
                    'current_balance': account.current_balance
                }
                )
                account.id = cursor.fetchone()[0]
        return account

    def get_by_num(self, accountNumber):
        with psycopg2.connect(host=self.host, database=self.database, user=self.user,
                        password=self.password) as db:
            with db.cursor() as cursor:
                cursor.execute("""
                    SELECT ID, AccountNum, CustomerID, CurrentBalance FROM account WHERE AccountNum=%(accountNumber)s
                    """, {
                        'accountNumber': accountNumber
                    }
                )
                account_row = cursor.fetchone()
                if account_row:
                    cursor.execute("""
                        SELECT ID, FirstName, LastName, AddressID, Email FROM customer WHERE ID=%(customer_id)s
                        """, {
                            'customer_id': account_row[2]
                        }
                    )
                    customer_row = cursor.fetchone()
                    if customer_row:
                        cursor.execute("""
                            SELECT ID, Address, City, State, ZipCode FROM address WHERE ID=%(address_id)s
                            """, {
                                'address_id': customer_row[3]
                            }
                        )
                    address_row = cursor.fetchone()
                    if address_row:
                        address = Address(id=address_row[0], address=address_row[1], city=address_row[2], state=address_row[3], zip_code=address_row[4])
                        customer = Customer(id=customer_row[0], first_name=customer_row[1], last_name=customer_row[2], address=address, email=customer_row[3])
                        return Account(id=account_row[0], account_num=account_row[1], customer=customer, current_balance=account_row[3])
                    else:
                        return None


    # def get_all_accounts(self):
    #     results = []
    #     addresses = []
    #     customers = []
    #     accounts = []
    #     with psycopg2.connect(host=self.host, database=self.database, user=self.user,
    #                     password=self.password) as db:
    #         with db.cursor() as cursor:
    #             cursor.execute("""
    #                 SELECT ID, Address, City, State, ZipCode FROM address
    #                 """
    #             )
    #             address_rows = cursor.fetchall()
    #             if address_rows:
    #                 for address_row in address_rows:
    #                     addresses.append(
    #                         Address(id=address_row[0], address=address_row[1], city=address_row[2], state=address_row[3], zip_code=address_row[4]))
    #                 cursor.execute("""
    #                     SELECT ID, FirstName, LastName, AddressID, Email FROM customer where AddressID=%(address_id)s
    #                     """,
    #                     {
    #                         'address_id': address_row[0]
    #                     }
    #                 )
    #                 customer_rows = cursor.fetchall()
    #                 if customer_rows:
    #                     for customer_row in customer_rows:
    #                         customer.append(
    #                             Customer(id=customer_row[0], first_name=customer_row[1], last_name=customer_row[2], address=addresses[customer_row[3]], email=customer_row[3])
    #                         )
    #                     cursor.execute("""
    #                         SELECT ID, AccountNum, CustomerID, CurrentBalance FROM account where CustomerID=%(customer_id)s 
    #                         """
    #                     ,
    #                     {
    #                         'customer_id': customer_row[0]
    #                     }
    #                     )
    #                     address_rows = cursor.fetchone()
    #                     if address_rows:
    #                         address = Address(id=address_row[0], address=address_row[1], city=address_row[2], state=address_row[3], zip_code=address_row[4])
    #                         customer = Customer(id=customer_row[0], first_name=customer_row[1], last_name=customer_row[2], address=address, email=customer_row[3])
    #                         return Account(id=account_row[0], account_num=account_row[1], customer=customer, current_balance=account_row[3])
    #                     else:
    #                         return None

## Need to work on finishing/updating these other definitions out

    def withdraw(self, amount, accountNumber):
        with psycopg2.connect(host=self.host, database=self.database, user=self.user,
                password=self.password) as db:
            with db.cursor() as cursor:
                cursor.execute("""
                    UPDATE account SET CurrentBalance = CurrentBalance - %(amount)s WHERE AccountNum=%(accountNumber)s
                    """,
                    {
                        'amount': amount,
                        'accountNumber': accountNumber
                    }
                )

    def deposit(self, amount, accountNumber):
        with psycopg2.connect(host=self.host, database=self.database, user=self.user,
                password=self.password) as db:
            with db.cursor() as cursor:
                cursor.execute(
                    """
                    UPDATE account SET CurrentBalance = CurrentBalance + %(amount)s WHERE AccountNum=%(accountNumber)s
                    """,
                    {
                        'amount': amount,
                        'accountNumber': accountNumber
                    }
                )

    def delete(self, account_num):
        with psycopg2.connect(host=self.host, database=self.database, user=self.user,
                password=self.password) as db:
            with db.cursor() as cursor:
                cursor.execute("""
                    DELETE FROM account WHERE AccountNum=%(account_num)s
                    DELETE FROM
                    """,
                    {
                        account_num: account_num
                    })