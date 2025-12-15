# Exercise 2: Statistics Methods (Class Methods)

**Read first:** `../lecture/class_methods.md`

**Prerequisites:** Complete Exercise 1 first (you'll use `format_currency()` here)

## Task

Add class methods to track bank-wide statistics in `hw_class_methods_bank_starter.py`.

**Why class methods?** These methods work with class-level data (like `total_accounts` and `total_deposits`) that's shared across all instances. They need `cls` to access class variables.

## Steps to Complete

**Add these 2 methods in the "EXERCISE 2: CLASS METHODS" section of the file.**

### Step 1: **`get_total_accounts(cls)`** - Class method
   - Returns: `"Total accounts: {count}"`
   - Access the class variable `total_accounts` using `cls`

### Step 2: **`get_total_deposits(cls)`** - Class method
   - Returns: `"Total customer deposits: {formatted}"`
   - Access the class variable `total_deposits` using `cls`
   - Use `cls.format_currency()` from Exercise 1 to format the amount

## Test

```bash
python3 test_exercise2.py
```
