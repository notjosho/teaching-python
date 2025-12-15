# Progressive BankAccount Class Exercise
# You will build this class across 3 exercises

class BankAccount:
    # Class variables - shared across all accounts
    bank_capital = 1_000_000  # Bank's starting money
    total_accounts = 0
    total_deposits = 0  # Customer deposits (bank's liability)

    def __init__(self, account_number, account_holder, initial_balance):
        # TODO: Add validation in Exercise 1 using validate_account_number()
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = initial_balance

        BankAccount.total_accounts += 1
        BankAccount.total_deposits += initial_balance

    # INSTANCE METHODS (already provided)
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            BankAccount.total_deposits += amount
            # Format manually for now (you'll create format_currency in Exercise 1)
            return f"Deposited ${amount:,.2f}. New balance: ${self.balance:,.2f}"
        return "Deposit amount must be positive"

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            BankAccount.total_deposits -= amount
            return f"Withdrew ${amount:,.2f}. New balance: ${self.balance:,.2f}"
        elif amount > self.balance:
            return "Insufficient funds"
        return "Withdrawal amount must be positive"

    def get_info(self):
        # Format manually for now (you'll create format_currency in Exercise 1)
        return f"Account {self.account_number} - {self.account_holder}: ${self.balance:,.2f}"

    # EXERCISE 1: STATIC METHODS - Utility functions (don't need self or cls)
    # TODO: Implement validate_account_number(account_number)
    # TODO: Implement format_currency(amount)

    # EXERCISE 2: CLASS METHODS - Work with class-level data
    # TODO: Implement get_total_accounts(cls)
    # TODO: Implement get_total_deposits(cls)

    # EXERCISE 3: MAGIC METHODS - Customize Python behavior
    # TODO: Implement __str__(self)
    # TODO: Implement __repr__(self)
    # TODO: Implement __eq__(self, other)
    # TODO: Implement __lt__(self, other) for balance comparison
