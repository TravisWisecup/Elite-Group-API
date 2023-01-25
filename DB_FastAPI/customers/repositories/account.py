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
                    SELECT ID, AccountNum, CustomerID, CurrentBalance FROM account WHERE AccountNum=%(accountNumber)s)
                    """, {
                        'accountNumber': accountNumber
                    }
                )
        row = cursor.fetchone()
        if row:
            customer = Customer(id=row[2], first_name='', last_name='', address='', email='')
            return Account(id=row[0], account_num=row[1], customer=customer, current_balance=row[3])
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
                Account(id=row[0], account_num=row[1], customer=row[2], current_balance=row)
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