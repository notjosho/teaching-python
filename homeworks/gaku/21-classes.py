class BankAccount:
    def __init__(self, name, money=0):
        self.owner = name
        self.balance = money

    def get_owner(self):
        return f"The owner is {self.owner}"

    def get_balance(self):
        return f"the balance is {self.balance}"

    def set_owner(self, name):
        self.owner = name

    def deposit(self, amount):
        if not isinstance(amount, (int, float)):
            return "Error: Amount must be a number"
        elif amount <= 0:
            return "Error: Amount must be greater than 0"
        self.balance += amount
        return f"Deposit successful. New balance: ${self.balance}"

    def withdraw(self, amount):
        if not isinstance(amount, (int, float)):
            return "Error: Amount must be a number"
        elif amount <= 0:
            return "Error: Amount must be greater than 0"
        elif self.balance < amount:
            return f"Error: Insufficient funds"
        self.balance -= amount
        return f"Withdrawal successful. New balance: ${self.balance}"


account1 = BankAccount("Juan")
account2 = BankAccount("Maria", 500)
account3 = BankAccount("Carlos", 100)

# Test Account 1: Default balance and operations
print(account1.get_owner())  # Expected: The owner is Juan
print(account1.get_balance())  # Expected: The balance is $0
print(account1.deposit(1000))  # Expected: Deposit successful. New balance: $1000
print(account1.get_balance())  # Expected: The balance is $1000
print(account1.withdraw(500))  # Expected: Withdrawal successful. New balance: $500
print(account1.get_balance())  # Expected: The balance is $500
account1.set_owner("Juan Perez")
print(account1.get_owner())  # Expected: The owner is Juan Perez

# Test Account 2: Initial balance
print(account2.get_owner())  # Expected: The owner is Maria
print(account2.get_balance())  # Expected: The balance is $500

# Test Account 3: Multiple operations with floats
print(account3.deposit(200.50))  # Expected: Deposit successful. New balance: $300.5
print(account3.withdraw(50.25))  # Expected: Withdrawal successful. New balance: $250.25

# Test Error Cases with Account 1
print(account1.deposit("hello"))  # Expected: Error: Amount must be a number
print(account1.deposit(0))  # Expected: Error: Amount must be greater than 0
print(account1.deposit(-100))  # Expected: Error: Amount must be greater than 0
print(account1.withdraw("world"))  # Expected: Error: Amount must be a number
print(account1.withdraw(0))  # Expected: Error: Amount must be greater than 0
print(account1.get_balance())  # Expected: The balance is $500
print(account1.withdraw(1000))  # Expected: Error: Insufficient funds
print(account1.get_balance())  # Expected: The balance is $500 (unchanged!)
