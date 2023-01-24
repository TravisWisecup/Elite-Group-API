import psycopg2
from customers.models.account import Account
from customers.models.customer import Customer
from customers.models.address import Address

class AccountRepository():
    db_name = 'customers.db'

    connection = psycopg2.connect(
        host="localhost", #possibly change later!!
        database="psycopgtest",  #possibly change later!!
        user="postgres", #possibly change later!!
        password=None,
    )
    connection.set_session(autocommit=True)

    def insert(self, account: Account):
        with cursor.connect() as cursor:
            cursor.execute('INSERT INTO [account] (AccountNum, CustomerID, CurrentBalance) VALUES \
                (?, ?, ?)', [account.account_num, account.customer_id, account.current_balance])
        account.id = cursor.lastrowid
        return account

    def retrieve_specific_account(self, accountNumber):
        with cursor.connect() as cursor:
            cursor.execute(
                'SELECT ID, AccountNum, CustomerID, CurrentBalance FROM [account] WHERE AccountNum=?;', [accountNumber])
        row = cursor.fetchone()
        if row:
            return Account(id=row[0], account_num=row[1], customer_id=row[2], current_balance=row[3])
        else:
            return None


    def retrieve_all_accounts(self):
        with cursor.connect() as cursor:
            cursor.execute(
                'SELECT * FROM account')
        accounts= cursor.fetchall()
        for row in accounts:
            print("ID: ", row[0])
            print("Account Number ", row[1])
            print("Customer ID: ", row[2])
            print("Current balance: ", row[3])
            print("\n")
        cursor.close()

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