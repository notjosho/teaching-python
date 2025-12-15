# Exercise 1: Utility Methods (Static Methods)

**Read first:** `../lecture/static_methods.md`

## Helpful Hints

### `.isdigit()` Method
Returns `True` if all characters in a string are digits (0-9), `False` otherwise.

Examples:
- `"12345".isdigit()` → `True`
- `"123a5".isdigit()` → `False` (contains letter)
- `"12.34".isdigit()` → `False` (contains period)
- `"".isdigit()` → `False` (empty string)

### `str()` Function
Converts a value to a string.

Examples:
- `str(12345)` → `"12345"`
- `str(123.45)` → `"123.45"`

### `len()` Function
Returns the number of items in a sequence (like a string or list).

Examples:
- `len("1234567890")` → `10`
- `len("123")` → `3`

### String Formatting: `f"${amount:,.2f}"`
Formats numbers as currency with commas and 2 decimal places.

Format breakdown:
- `:,` - adds commas as thousand separators
- `.2f` - displays exactly 2 decimal places

Examples:
- `f"${1234567.89:,.2f}"` → `"$1,234,567.89"`
- `f"${100:,.2f}"` → `"$100.00"`

## Task

Build utility methods for the `BankAccount` class in `hw_class_methods_bank_starter.py`.

These will be used in Exercise 2.

**Why static methods?** These are utility functions that don't need access to instance data (`self`) or class data (`cls`). They're helpers that could work independently but belong with the class logically.

## Steps to Complete

### STEP 1-2: Create Static Methods

**Add these 2 methods in the "EXERCISE 1: STATIC METHODS" section of the file.**

#### Step 1: **`validate_account_number(account_number)`** - Static method
   - Returns: `True` if valid, `False` otherwise
   - Valid: exactly 10 digits
   - See hints: `str()`, `.isdigit()`, `len()`

#### Step 2: **`format_currency(amount)`** - Static method
   - Returns: `"$X,XXX.XX"`
   - Example: `1234567.89` → `"$1,234,567.89"`
   - See hints: currency formatting with `f"${amount:,.2f}"`

### STEP 3: Update Existing Code

**Modify the `__init__()` method at the top of the class to add validation.**

#### Step 3: **Update `__init__()` to use validation**
   - Add validation at the start of `__init__()` before setting attributes
   - Use `validate_account_number()` to check the account number
   - If invalid, raise: `ValueError("Invalid account number format")`

## Test

```bash
python3 test_exercise1.py
```

**Next:** Exercise 2 will use these utilities!
