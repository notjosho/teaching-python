class BankAccount:
    def __init__(self, owner, balance=0):
        self._owner = owner
        self._balance = balance
   
    def set_owner(self, owner):
        self._owner = owner

    def set_balance(self, balance):
        self._balance = balance

    def get_owner(self):
        return f'The owner is {self._owner}'
    
    def get_balance(self):
        return f'The balance is ${self._balance}'
    
    def deposit(self, amount):
        if not isinstance(amount, (int, float)):
            return "Error: Amount must be a number"
        if amount <= 0:
            return "Error: Amount must be greater than 0"
        
        self._balance += amount
        return f"Deposit successful. New balance: ${self._balance}"

    def withdraw(self, amount):
        if not isinstance(amount, (int, float)):
            return "Error: Amount must be a number"
        if amount <= 0:
            return "Error: Amount must be greater than 0"
        if amount > self._balance:
            return "Error: Insufficient funds"
        
        self._balance -= amount
        return f"Withdrawal successful. New balance: ${self._balance}"

# Create 3 different accounts
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
    