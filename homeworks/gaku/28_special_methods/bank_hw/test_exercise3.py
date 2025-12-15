#!/usr/bin/env python3
# Test file for Exercise 3: Magic Methods - Banking System
#
# PREREQUISITE: Complete Exercise 1 first!
# This test assumes Exercise 1's validation methods work correctly.
# If you get ValueError when creating accounts, complete Exercise 1 first.

from hw_class_methods_bank import BankAccount

all_tests_passed = True

print("=" * 60)
print("EXERCISE 3: MAGIC METHODS TEST - BANKING SYSTEM")
print("=" * 60)

# Create test accounts
account1 = BankAccount("1234567890", "Alice Johnson", 5000)
account2 = BankAccount("9876543210", "Bob Smith", 10000)
account3 = BankAccount("5555555555", "Charlie Brown", 3000)
account4 = BankAccount("1234567890", "Duplicate Account", 1000)  # Same account number as account1

print("\n" + "=" * 60)
print("TEST 1: __str__() - user-friendly representation")
print("=" * 60)
try:
    result = str(account1)
    expected = "Alice Johnson's Account (1234567890): $5,000.00"
    print(f"str(account1): {result}")
    print(f"Expected:      {expected}")

    if result == expected:
        print("✓ PASS")
    else:
        print("✗ FAIL - String doesn't match expected format")
        all_tests_passed = False
except AttributeError:
    print("✗ FAIL: Method __str__() not implemented")
    all_tests_passed = False

print("\n" + "=" * 60)
print("TEST 2: __str__() - different account")
print("=" * 60)
try:
    result = str(account2)
    expected = "Bob Smith's Account (9876543210): $10,000.00"
    print(f"str(account2): {result}")
    print(f"Expected:      {expected}")

    if result == expected:
        print("✓ PASS")
    else:
        print("✗ FAIL - String doesn't match expected format")
        all_tests_passed = False
except AttributeError:
    print("✗ FAIL: Method __str__() not implemented")
    all_tests_passed = False

print("\n" + "=" * 60)
print("TEST 3: __repr__() - developer representation")
print("=" * 60)
try:
    result = repr(account1)
    expected = "BankAccount(account_number='1234567890', account_holder='Alice Johnson', balance=5000)"
    print(f"repr(account1): {result}")
    print(f"Expected:       {expected}")

    if result == expected:
        print("✓ PASS")
    else:
        print("✗ FAIL - Representation doesn't match expected format")
        all_tests_passed = False
except AttributeError:
    print("✗ FAIL: Method __repr__() not implemented")
    all_tests_passed = False

print("\n" + "=" * 60)
print("TEST 4: __repr__() - different account")
print("=" * 60)
try:
    result = repr(account3)
    expected = "BankAccount(account_number='5555555555', account_holder='Charlie Brown', balance=3000)"
    print(f"repr(account3): {result}")
    print(f"Expected:       {expected}")

    if result == expected:
        print("✓ PASS")
    else:
        print("✗ FAIL - Representation doesn't match expected format")
        all_tests_passed = False
except AttributeError:
    print("✗ FAIL: Method __repr__() not implemented")
    all_tests_passed = False

print("\n" + "=" * 60)
print("TEST 5: __eq__() - same account number")
print("=" * 60)
try:
    result = (account1 == account4)
    print(f"account1.account_number: {account1.account_number}")
    print(f"account4.account_number: {account4.account_number}")
    print(f"account1 == account4: {result}")

    if result == True:
        print("✓ PASS - Correctly identifies same account number")
    else:
        print("✗ FAIL - Should be True for same account number")
        all_tests_passed = False
except AttributeError:
    print("✗ FAIL: Method __eq__() not implemented")
    all_tests_passed = False
except Exception as e:
    print(f"✗ FAIL: Error in __eq__() - {e}")
    all_tests_passed = False

print("\n" + "=" * 60)
print("TEST 6: __eq__() - different account numbers")
print("=" * 60)
try:
    result = (account1 == account2)
    print(f"account1.account_number: {account1.account_number}")
    print(f"account2.account_number: {account2.account_number}")
    print(f"account1 == account2: {result}")

    if result == False:
        print("✓ PASS - Correctly identifies different account numbers")
    else:
        print("✗ FAIL - Should be False for different account numbers")
        all_tests_passed = False
except AttributeError:
    print("✗ FAIL: Method __eq__() not implemented")
    all_tests_passed = False
except Exception as e:
    print(f"✗ FAIL: Error in __eq__() - {e}")
    all_tests_passed = False

print("\n" + "=" * 60)
print("TEST 7: __lt__() - balance comparison (less than)")
print("=" * 60)
try:
    result = (account3 < account1)
    print(f"account3.balance: ${account3.balance:,.2f}")
    print(f"account1.balance: ${account1.balance:,.2f}")
    print(f"account3 < account1: {result}")

    if result == True:
        print("✓ PASS - Correctly compares balances (3000 < 5000)")
    else:
        print("✗ FAIL - Should be True when balance 3000 < 5000")
        all_tests_passed = False
except AttributeError:
    print("✗ FAIL: Method __lt__() not implemented")
    all_tests_passed = False
except Exception as e:
    print(f"✗ FAIL: Error in __lt__() - {e}")
    all_tests_passed = False

print("\n" + "=" * 60)
print("TEST 8: __lt__() - balance comparison (not less than)")
print("=" * 60)
try:
    result = (account2 < account1)
    print(f"account2.balance: ${account2.balance:,.2f}")
    print(f"account1.balance: ${account1.balance:,.2f}")
    print(f"account2 < account1: {result}")

    if result == False:
        print("✓ PASS - Correctly compares balances (10000 not < 5000)")
    else:
        print("✗ FAIL - Should be False when balance 10000 not < 5000")
        all_tests_passed = False
except AttributeError:
    print("✗ FAIL: Method __lt__() not implemented")
    all_tests_passed = False
except Exception as e:
    print(f"✗ FAIL: Error in __lt__() - {e}")
    all_tests_passed = False

print("\n" + "=" * 60)
print("TEST 9: Sorting with __lt__()")
print("=" * 60)
try:
    accounts = [account2, account1, account3]  # Balances: 10000, 5000, 3000
    sorted_accounts = sorted(accounts)

    print(f"Original order: {[acc.account_holder for acc in accounts]}")
    print(f"Sorted order:   {[acc.account_holder for acc in sorted_accounts]}")
    print(f"Balances:       {[f'${acc.balance:,.2f}' for acc in sorted_accounts]}")

    balances_sorted = [acc.balance for acc in sorted_accounts]
    if balances_sorted == [3000, 5000, 10000]:
        print("✓ PASS - Accounts sorted correctly by balance")
    else:
        print(f"✗ FAIL - Expected balances [3000, 5000, 10000], got {balances_sorted}")
        all_tests_passed = False
except AttributeError:
    print("✗ FAIL: Method __lt__() not implemented")
    all_tests_passed = False
except Exception as e:
    print(f"✗ FAIL: Error in sorting - {e}")
    all_tests_passed = False

print("\n" + "=" * 60)
print("TEST 10: print() uses __str__()")
print("=" * 60)
try:
    print("Calling print(account1):")
    print(account1)
    print("\nIf you see the format \"{holder}'s Account ({number}): ${balance}\", __str__ works!")
    print("✓ PASS - print() successfully uses __str__()")
except AttributeError:
    print("✗ FAIL: Method __str__() not implemented")
    all_tests_passed = False

print("\n" + "=" * 60)
if all_tests_passed:
    print("EXERCISE 3 COMPLETE!")
else:
    print("EXERCISE 3 FAILED - Fix the errors above and try again")
print("=" * 60)

if all_tests_passed:
    print("\nCongratulations! You've completed all three banking exercises!")
    print("\nYou now understand:")
    print("  - Instance methods: for account-specific operations")
    print("  - Class methods: for bank-wide statistics and data")
    print("  - Static methods: for utility functions")
    print("  - Magic methods: for customizing Python behavior")
    print("\nYou have a fully-featured BankAccount class!")
    print("\nBank error in your favor - you've mastered OOP! Collect $200.")
    print("""
@@@@@@@@@@@@@@@       .@@@@@@@@@@# %@%
@@@@@@@@@@@+   @@@@     @@@@@@@@@ @  @
@@@@@@@@@   @@@@@@@@    =@@@@@@@@ @ +@
@@@@@@@      @@@@@@@@    =@@@@@@@ =@
@@@@@-        @@@@   .     @@@@  @  %%
@@@@@           :@@@@@@     %:  @@@@
@@@@@  #.       %@@@@@.        @@@@@@@
@@@@@@@  :  -       %@@@@@@@-   @@@@@@
@@@@@@@@      -@  @=.@@@@@@@@@@. @@@@@
@@@@@@@@@  +@   @@@@@@@@@@@@@@ +  @@@@
@@@@@@@@  @  *@@@@@@@@ @@@@@@@@@@ @@@@
  +@@@@  @  @@  @@@@@@@@@@@+ @@@@  @=@
      @. #    @@@@@@@@@@@@@-         @
            @@@@@@@@@@@  @@@@@@@@@@  @
              =*@@  #  @@@@@@#@@@  @@@
                 @@  @@@@@  .@@  @@@@@
@=                 *@@. .@@@@*  @@@@@@
@@@@              %@
@@@@@@             @@ @@@@@@
""")
