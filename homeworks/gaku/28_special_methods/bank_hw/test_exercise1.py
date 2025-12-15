#!/usr/bin/env python3
# Test file for Exercise 1: Static Methods - Banking System

from hw_class_methods_bank import BankAccount

all_tests_passed = True

print("=" * 60)
print("EXERCISE 1: STATIC METHODS TEST - BANKING SYSTEM")
print("=" * 60)

print("\n" + "=" * 60)
print("STEP 1: Testing validate_account_number()")
print("=" * 60)
print("\n" + "=" * 60)
print("TEST 1: validate_account_number() - valid accounts")
print("=" * 60)
try:
    test_cases = [
        ("1234567890", True),
        ("9876543210", True),
        ("0000000000", True),
        (1234567890, True),  # Integer input
    ]

    all_passed = True
    for acc_num, expected in test_cases:
        result = BankAccount.validate_account_number(acc_num)
        status = "✓" if result == expected else "✗"
        print(f"{status} validate_account_number('{acc_num}') = {result} (expected {expected})")
        if result != expected:
            all_passed = False

    if all_passed:
        print("✓ PASS - All valid account numbers accepted")
    else:
        print("✗ FAIL - Some valid account numbers rejected")
        all_tests_passed = False
except AttributeError:
    print("✗ FAIL: Method validate_account_number() not implemented")
    all_tests_passed = False

print("\n" + "=" * 60)
print("TEST 2: validate_account_number() - invalid accounts")
print("=" * 60)
try:
    test_cases = [
        ("123", False),  # Too short
        ("12345678901", False),  # Too long
        ("12345abcde", False),  # Contains letters
        ("123-456-789", False),  # Contains dashes
        ("", False),  # Empty
        ("abc", False),  # Only letters
    ]

    all_passed = True
    for acc_num, expected in test_cases:
        result = BankAccount.validate_account_number(acc_num)
        status = "✓" if result == expected else "✗"
        print(f"{status} validate_account_number('{acc_num}') = {result} (expected {expected})")
        if result != expected:
            all_passed = False

    if all_passed:
        print("✓ PASS - All invalid account numbers rejected")
    else:
        print("✗ FAIL - Some invalid account numbers accepted")
        all_tests_passed = False
except AttributeError:
    print("✗ FAIL: Method validate_account_number() not implemented")
    all_tests_passed = False

print("\n" + "=" * 60)
print("STEP 2: Testing format_currency()")
print("=" * 60)
print("\n" + "=" * 60)
print("TEST 3: format_currency() - currency formatting")
print("=" * 60)
try:
    test_cases = [
        (1000, "$1,000.00"),
        (1234567.89, "$1,234,567.89"),
        (0, "$0.00"),
        (99.9, "$99.90"),
        (1000000, "$1,000,000.00"),
        (5.5, "$5.50"),
    ]

    all_passed = True
    for amount, expected in test_cases:
        result = BankAccount.format_currency(amount)
        status = "✓" if result == expected else "✗"
        print(f"{status} format_currency({amount}) = '{result}' (expected '{expected}')")
        if result != expected:
            all_passed = False

    if all_passed:
        print("✓ PASS - Currency formatting correct")
    else:
        print("✗ FAIL - Some currency formatting incorrect")
        all_tests_passed = False
except AttributeError:
    print("✗ FAIL: Method format_currency() not implemented")
    all_tests_passed = False

print("\n" + "=" * 60)
print("STEP 3: Testing __init__() validation")
print("=" * 60)
print("\n" + "=" * 60)
print("TEST 4: __init__() validation - invalid account number")
print("=" * 60)
try:
    # Test too short
    try:
        account = BankAccount("123", "Alice", 1000)
        print("✗ FAIL - Should reject account number '123' (too short)")
        all_tests_passed = False
    except ValueError as e:
        if "Invalid account number" in str(e):
            print(f"✓ PASS - Rejected '123': {e}")
        else:
            print(f"✗ FAIL - Wrong error message: {e}")
            all_tests_passed = False

    # Test too long
    try:
        account = BankAccount("12345678901", "Alice", 1000)
        print("✗ FAIL - Should reject account number (too long)")
        all_tests_passed = False
    except ValueError as e:
        if "Invalid account number" in str(e):
            print(f"✓ PASS - Rejected long number: {e}")
        else:
            print(f"✗ FAIL - Wrong error message: {e}")
            all_tests_passed = False

    # Test with letters
    try:
        account = BankAccount("123456789A", "Alice", 1000)
        print("✗ FAIL - Should reject account number with letters")
        all_tests_passed = False
    except ValueError as e:
        if "Invalid account number" in str(e):
            print(f"✓ PASS - Rejected '123456789A': {e}")
        else:
            print(f"✗ FAIL - Wrong error message: {e}")
            all_tests_passed = False

    # Test with special characters
    try:
        account = BankAccount("1234-5678-90", "Alice", 1000)
        print("✗ FAIL - Should reject account number with dashes")
        all_tests_passed = False
    except ValueError as e:
        if "Invalid account number" in str(e):
            print(f"✓ PASS - Rejected '1234-5678-90': {e}")
        else:
            print(f"✗ FAIL - Wrong error message: {e}")
            all_tests_passed = False

except Exception as e:
    print(f"✗ FAIL: Validation not implemented properly - {e}")
    all_tests_passed = False

print("\n" + "=" * 60)
print("TEST 5: __init__() validation - valid account number accepted")
print("=" * 60)
try:
    account = BankAccount("1234567890", "Alice Johnson", 5000)
    print(f"✓ PASS - Created account: {account.account_holder} - Account #{account.account_number}")
except Exception as e:
    print(f"✗ FAIL: Valid data should be accepted - {e}")
    all_tests_passed = False

print("\n" + "=" * 60)
if all_tests_passed:
    print("EXERCISE 1 COMPLETE!")
else:
    print("EXERCISE 1 FAILED - Fix the errors above and try again")
print("=" * 60)
