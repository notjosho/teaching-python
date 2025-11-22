# Duck Typing Exercise: Payment Processing System

## What is Duck Typing?

Duck typing is a programming concept where an object's suitability is determined by the presence of certain methods and properties, rather than by its actual type. The name comes from the phrase:

> "If it walks like a duck and quacks like a duck, then it must be a duck."
> In Python, this means you can use any object in a function as long as it has the required methods and attributes - no inheritance or type checking needed.

## Duck Typing Exercise

Build a payment processing system with four different payment method classes that share the same interface (methods and attributes) without using inheritance.

### Requirements

Each payment class must have:

- An attribute `requires_verification` (boolean)
- A method `process_payment(self, amount)` that returns a confirmation string
- A method `get_transaction_fee(self, amount)` that returns the fee as a number

### 1. Create the CreditCard Class

- `requires_verification`: True
- `process_payment`: Returns `"Processing $XX.XX via credit card"`
- `get_transaction_fee`: 2.5% of the amount (multiply by 0.025)

### 2. Create the PayPal Class

- `requires_verification`: True
- `process_payment`: Returns `"Processing $XX.XX via PayPal"`
- `get_transaction_fee`: 3% of the amount plus $0.30 (multiply by 0.03, then add 0.30)

### 3. Create the Bitcoin Class

- `requires_verification`: False
- `process_payment`: Returns `"Processing $XX.XX via Bitcoin wallet"`
- `get_transaction_fee`: 1% of the amount (multiply by 0.01)

### 4. Create the BankTransfer Class

- `requires_verification`: True
- `process_payment`: Returns `"Processing $XX.XX via bank transfer"`
- `get_transaction_fee`: Flat fee of $5.00 (always returns 5.00)

### 5. Create the process_all_payments Function

Write a function `process_all_payments(payment_methods, amounts)` that:

- Takes a list of payment method objects and a list of amounts
- For each amount, builds a formatted string that includes:
  - A header showing the payment amount
  - For each payment method:
    - The confirmation message from `process_payment`
    - The transaction fee from `get_transaction_fee`
    - Whether verification is required from `requires_verification`
- Prints the formatted output string
- Returns the formatted output string
  Notice that this function does NOT check the type of each payment method. It simply calls the expected methods on each object. This is duck typing in action.

## Fee Calculation Reference

| Payment Method | Fee Formula             | Example ($100) |
| -------------- | ----------------------- | -------------- |
| CreditCard     | amount \* 0.025         | $2.50          |
| PayPal         | (amount \* 0.03) + 0.30 | $3.30          |
| Bitcoin        | amount \* 0.01          | $1.00          |
| BankTransfer   | 5.00 (flat)             | $5.00          |

## Why This is Duck Typing

1. **No inheritance**: The four classes do not inherit from a common parent class
2. **No type checking**: The `process_all_payments` function never uses `isinstance()` or checks the type of objects
3. **Behavior-based**: Objects are used based on what methods they have, not what class they belong to
4. **Flexibility**: Any new payment class with the same methods would work automatically
   This pattern is common in Python and allows for flexible, extensible code without rigid class hierarchies.
