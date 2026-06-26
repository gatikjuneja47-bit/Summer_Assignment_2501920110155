print("ATM Simulator")
account_balance = 10000
pin = input("Enter your PIN: ")

if pin != "1302":
    print("Incorrect PIN. Access denied.")
    exit()
switch = input("enter the type of transaction you want to perform: \n1. Withdraw\n2. Deposit\n3. Check Balance\n")
if switch == "1":
    amount = int(input("enter the amount you want to withdraw: "))
    if amount > account_balance:
        print("insufficient balance")
    else:
        account_balance -= amount
        print("withdrawal successful\ncurrent balance: ", account_balance)
elif switch == "2":
    amount = int(input("enter the amount you want to deposit: "))
    account_balance += amount
    print("deposit successful\ncurrent balance: ", account_balance)
elif switch == "3":
    print("current balance: ", account_balance)
else:
    print("invalid transaction")
print("Thank you for using the ATM")