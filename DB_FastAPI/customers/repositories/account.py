import psycopg2
from customers.models.account import Account
from customers.models.customer import Customer
from customers.models.address import Address

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


    def get_all_accounts(self):
        results = []
        with psycopg2.connect(host=self.host, database=self.database, user=self.user,
                        password=self.password) as db:
            with db.cursor() as cursor:
                cursor.execute("""
                    SELECT ID, AccountNum, CustomerID, CurrentBalance FROM account
                    """)
        accounts= cursor.fetchall()
        for row in accounts:
            results.append(
                Account(id=row[0], account_num=row[1], customer=row[2], current_balance=row[3])
            )
        cursor.close()

## Need to work on finishing/updating these other definitions out

    def withdraw(self, amount, accountNumber):
        with cursor.connect() as cursor:
            cursor.execute(
                'UPDATE account SET CurrentBalance = CurrentBalance - amount WHERE AccountNum=?;', [accountNumber])
            cursor.close()

    def deposit(self, amount, accountNumber):
        with cursor.connect() as cursor:
            cursor.execute(
                'UPDATE account SET CurrentBalance = CurrentBalance + amount WHERE AccountNum=?;', [accountNumber])
            cursor.close()

    def delete(self, id):
        with cursor.connect() as cursor:
            cursor.execute(
                'DELETE FROM [account] WHERE ID=?;', [id])