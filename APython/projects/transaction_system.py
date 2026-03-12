# Simple List-Based Transaction System

def see_balance(transactions):
    """Display the current balance based on the transaction list."""
    balance = sum(transactions)
    print(f"Current Balance: {balance}")
    return balance

def deposit(transactions, amount):
    """Add a deposit to the transaction list."""
    if amount > 0:
        transactions.append(amount)
        print(f"Deposited: {amount}")
    else:
        print("Deposit amount must be positive.")

def withdraw(transactions, amount):
    """Withdraw an amount if sufficient balance exists."""
    balance = sum(transactions)
    if 0 < amount <= balance:
        transactions.append(-amount)
        print(f"Withdrew: {amount}")
    else:
        print("Insufficient balance or invalid amount.")

transactions = []
while True:
    print("\nOptions: 1) See Balance 2) Deposit 3) Withdraw 4) Exit")
    choice = input("Enter your choice (1-4): ")
    if choice == '1':
        see_balance(transactions)
    elif choice == '2':
        amount = float(input("Enter deposit amount: "))
        deposit(transactions, amount)
    elif choice == '3':
        amount = float(input("Enter withdrawal amount: "))
        withdraw(transactions, amount)
    elif choice == '4':
        print("Exiting. Thank you!")
        break
    else:
        print("Invalid choice. Please try again.")
