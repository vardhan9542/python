balance = 1000

def deposit(amount):
    global balance
    balance += amount

def withdraw(amount):
    global balance

    if amount <= balance:
        balance -= amount
        print("Withdrawal successful")
    else:
        print("Insufficient funds")

deposit(500)
print("Balance:", balance)

withdraw(300)
print("Balance:", balance)

withdraw(2000)
print("Balance:", balance)

# Output:
# Balance: 1500
# Withdrawal successful
# Balance: 1200
# Insufficient funds
# Balance: 1200