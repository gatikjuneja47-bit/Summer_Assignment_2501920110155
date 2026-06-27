class BankAccount:
    def __init__(self, account_number, account_holder, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Deposit amount must be positive.")
    def withdraw(self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                print(f"Withdrew ${amount}. New balance: ${self.balance}")
            else:
                print("Insufficient Balance")
        else:
            print("Withdrawal amount must be positive.")
    def display_balance(self):
        print(f"Account Number: {self.account_number}, Account Holder: {self.account_holder}, Balance: ${self.balance}")
print("Welcome to the Bank Account Management System!")
account_number = input("Enter account number: ")
account_holder = input("Enter account holder name: ")
account = BankAccount(account_number, account_holder)
while True:
    print("\nMenu:")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Display Balance")
    print("4. Exit")
    choice = input("Enter your choice (1-4): ")
    if choice == '1':
        amount = float(input("Enter amount to deposit: "))
        account.deposit(amount)
    elif choice == '2':
        amount = float(input("Enter amount to withdraw: "))
        account.withdraw(amount)
    elif choice == '3':
        account.display_balance()
    elif choice == '4':
        print("Exiting the Bank Account Management System. Thank You")
        break
    else:
        print("Invalid choice. Please try again.")