#3.Banking System with Transactions Simulate real-time transactions between bank accounts. 
#Handle errors like overdraft, transaction timeout, incorrect account numbers. 
import time
class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.balance += amount
    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount
class BankingSystem:  
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_number, initial_balance=0):
        if account_number in self.accounts:
            raise ValueError("Account already exists")
        self.accounts[account_number] = BankAccount(account_number, initial_balance)

    def transfer(self, from_account, to_account, amount):
        if from_account not in self.accounts or to_account not in self.accounts:
            raise ValueError("Invalid account number")
        if amount <= 0:
            raise ValueError("Transfer amount must be positive")
        # Simulate transaction timeout
        time.sleep(1)
        self.accounts[from_account].withdraw(amount)
        self.accounts[to_account].deposit(amount)
# test the banking system
if __name__ == "__main__":
    banking_system = BankingSystem()
    try:
        print("Creating accounts...")
        print("Enter account number for account 1: ")
        acc1 = input()
        print("Enter initial balance for account 1: ")
        bal1 = float(input())
        banking_system.create_account(acc1, bal1)
        print("Enter account number for account 2: ")
        acc2 = input()
        print("Enter initial balance for account 2: ")
        bal2 = float(input())
        banking_system.create_account(acc2, bal2)
        print("Transferring funds...")
        print("Enter amount to transfer from {} to {}: ".format(acc1, acc2))
        amount = float(input())
        banking_system.transfer(acc1, acc2, amount)
        print("Transfer completed successfully.")
        print("Account {} balance: {}".format(acc1, banking_system.accounts[acc1].balance))
        print("Account {} balance: {}".format(acc2, banking_system.accounts[acc2].balance))
    except ValueError as e:
        print(e)
