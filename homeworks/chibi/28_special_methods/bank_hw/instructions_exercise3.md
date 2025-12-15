# Exercise 3: Magic Methods

**Read first:** `../lecture/magic_methods.md`

## Task

Add magic methods to the `BankAccount` class in `hw_class_methods_bank_starter.py`:

**Why magic methods?** These special methods let you customize how Python behaves with your objects - how they're printed, compared, and sorted. Python automatically calls these methods in specific situations.

### Methods to Implement

1. **`__str__(self)`** - Magic method
   - Returns: `"{holder}'s Account ({number}): {formatted_balance}"`
   - Example: `"Alice's Account (1234567890): $5,000.00"`
   - Use `format_currency()` static method

2. **`__repr__(self)`** - Magic method
   - Returns: `"BankAccount(account_number='{number}', account_holder='{holder}', balance={balance})"`
   - Example: `"BankAccount(account_number='1234567890', account_holder='Alice', balance=5000)"`

3. **`__eq__(self, other)`** - Magic method
   - Returns: `True` if same account number
   - Two accounts with same number are the same account

4. **`__lt__(self, other)`** - Magic method
   - Returns: `True` if `self.balance < other.balance`
   - Enables sorting by balance

## Test

```bash
python3 test_exercise3.py
```
