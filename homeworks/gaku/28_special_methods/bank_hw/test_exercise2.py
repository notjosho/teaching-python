#!/usr/bin/env python3
# Test file for Exercise 2: Class Methods - Banking System
#
# PREREQUISITE: Complete Exercise 1 first!
# This test assumes Exercise 1's validation methods work correctly.
# If you get ValueError when creating accounts, complete Exercise 1 first.

from hw_class_methods_bank import BankAccount

all_tests_passed = True

print("=" * 60)
print("EXERCISE 2: CLASS METHODS TEST - BANKING SYSTEM")
print("=" * 60)

# Reset class variables for testing
BankAccount.total_accounts = 0
BankAccount.total_deposits = 0
BankAccount.bank_capital = 1_000_000

# Create test accounts
print("\nCreating accounts...")
account1 = BankAccount("1234567890", "Alice Johnson", 5000)
account2 = BankAccount("9876543210", "Bob Smith", 3000)
account3 = BankAccount("5555555555", "Charlie Brown", 10000)

print("\n" + "=" * 60)
print("TEST 1: get_total_accounts()")
print("=" * 60)
try:
    result = BankAccount.get_total_accounts()
    print(f"Result: {result}")
    assert result == "Total accounts: 3", f"Expected 'Total accounts: 3', got '{result}'"
    print("✓ PASS")
except AttributeError:
    print("✗ FAIL: Method get_total_accounts() not implemented")
    all_tests_passed = False
except AssertionError as e:
    print(f"✗ FAIL: {e}")
    all_tests_passed = False

print("\n" + "=" * 60)
print("TEST 2: get_total_deposits() - initial deposits")
print("=" * 60)
try:
    result = BankAccount.get_total_deposits()
    print(f"Result: {result}")
    assert result == "Total customer deposits: $18,000.00", f"Expected 'Total customer deposits: $18,000.00', got '{result}'"
    print("✓ PASS")
except AttributeError:
    print("✗ FAIL: Method get_total_deposits() not implemented")
    all_tests_passed = False
except AssertionError as e:
    print(f"✗ FAIL: {e}")
    all_tests_passed = False

# Make some transactions
print("\n" + "=" * 60)
print("Making transactions...")
print("=" * 60)
account1.deposit(1500)
account2.withdraw(500)

print("\n" + "=" * 60)
print("TEST 3: get_total_deposits() - after transactions")
print("=" * 60)
try:
    result = BankAccount.get_total_deposits()
    print(f"Result: {result}")
    assert result == "Total customer deposits: $19,000.00", f"Expected 'Total customer deposits: $19,000.00', got '{result}'"
    print("✓ PASS")
except AttributeError:
    print("✗ FAIL: Method get_total_deposits() not implemented")
    all_tests_passed = False
except AssertionError as e:
    print(f"✗ FAIL: {e}")
    all_tests_passed = False

print("\n" + "=" * 60)
if all_tests_passed:
    print("EXERCISE 2 COMPLETE!")
else:
    print("EXERCISE 2 FAILED - Fix the errors above and try again")
print("=" * 60)
