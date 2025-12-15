#!/usr/bin/env python3
# Test file for Exercise 3: Magic Methods
#
# PREREQUISITE: Complete Exercise 1 first!
# This test assumes Exercise 1's validation methods work correctly.
# If you get ValueError when creating champions, complete Exercise 1 first.

from hw_class_methods_game import Champion

all_tests_passed = True

print("=" * 60)
print("EXERCISE 3: MAGIC METHODS TEST - League of Legends")
print("=" * 60)

# Create test champions
champ1 = Champion("Faker", "Zed", "Mid")
champ1.level = 5

champ2 = Champion("TheShy", "Fiora", "Top")
champ2.level = 3

champ3 = Champion("Uzi", "Vayne", "ADC")
champ3.level = 7

print("\n" + "=" * 60)
print("TEST 1: __repr__() - developer representation")
print("=" * 60)
try:
    result = repr(champ1)
    print(f"repr(champ1): {result}")

    expected = "Champion(summoner_name='Faker', champion_name='Zed', role='Mid', level=5)"
    assert result == expected, f"Expected '{expected}', got '{result}'"
    print("✓ PASS - __repr__() returns correct format")
except AttributeError:
    print("✗ FAIL: Method __repr__() not implemented")
    all_tests_passed = False
except AssertionError as e:
    print(f"✗ FAIL: {e}")
    all_tests_passed = False

print("\n" + "=" * 60)
print("TEST 2: __eq__() - same summoner name (different case)")
print("=" * 60)
try:
    champ4 = Champion("FAKER", "Azir", "Mid")
    result = champ1 == champ4

    print(f"champ1 summoner: '{champ1.summoner_name}'")
    print(f"champ4 summoner: '{champ4.summoner_name}'")
    print(f"champ1 == champ4: {result}")

    assert result == True, "Expected True (same summoner name, case-insensitive)"
    print("✓ PASS - __eq__() works with case-insensitive comparison")
except AttributeError:
    print("✗ FAIL: Method __eq__() not implemented")
    all_tests_passed = False
except AssertionError as e:
    print(f"✗ FAIL: {e}")
    all_tests_passed = False

print("\n" + "=" * 60)
print("TEST 3: __eq__() - different summoner names")
print("=" * 60)
try:
    result = champ1 == champ2

    print(f"champ1 summoner: '{champ1.summoner_name}'")
    print(f"champ2 summoner: '{champ2.summoner_name}'")
    print(f"champ1 == champ2: {result}")

    assert result == False, "Expected False (different summoner names)"
    print("✓ PASS - __eq__() correctly identifies different summoners")
except AttributeError:
    print("✗ FAIL: Method __eq__() not implemented")
    all_tests_passed = False
except AssertionError as e:
    print(f"✗ FAIL: {e}")
    all_tests_passed = False

print("\n" + "=" * 60)
print("TEST 4: __lt__() - level comparison")
print("=" * 60)
try:
    result1 = champ2 < champ1  # Level 3 < Level 5
    result2 = champ1 < champ3  # Level 5 < Level 7

    print(f"champ2 (Level {champ2.level}) < champ1 (Level {champ1.level}): {result1}")
    print(f"champ1 (Level {champ1.level}) < champ3 (Level {champ3.level}): {result2}")

    assert result1 == True, "Expected True (3 < 5)"
    assert result2 == True, "Expected True (5 < 7)"
    print("✓ PASS - __lt__() correctly compares levels")
except AttributeError:
    print("✗ FAIL: Method __lt__() not implemented")
    all_tests_passed = False
except AssertionError as e:
    print(f"✗ FAIL: {e}")
    all_tests_passed = False

print("\n" + "=" * 60)
print("TEST 5: sorting champions by level using __lt__()")
print("=" * 60)
try:
    champions = [champ1, champ2, champ3]
    sorted_champs = sorted(champions)

    print("Original order:")
    for c in champions:
        print(f"  {c.summoner_name} - Level {c.level}")

    print("\nSorted order (by level):")
    for c in sorted_champs:
        print(f"  {c.summoner_name} - Level {c.level}")

    # Check if sorted correctly (ascending order)
    assert sorted_champs[0] == champ2, "First should be TheShy (Level 3)"
    assert sorted_champs[1] == champ1, "Second should be Faker (Level 5)"
    assert sorted_champs[2] == champ3, "Third should be Uzi (Level 7)"
    print("✓ PASS - Sorting works correctly using __lt__()")
except AttributeError:
    print("✗ FAIL: Method __lt__() not implemented")
    all_tests_passed = False
except AssertionError as e:
    print(f"✗ FAIL: {e}")
    all_tests_passed = False

print("\n" + "=" * 60)
print("TEST 6: __str__() - user-friendly string")
print("=" * 60)
try:
    result = str(champ1)
    print(f"str(champ1): {result}")

    expected = "Faker playing Zed (Mid) - Level 5"
    assert result == expected, f"Expected '{expected}', got '{result}'"
    print("✓ PASS - __str__() returns correct format")
except AttributeError:
    print("✗ FAIL: Method __str__() not implemented")
    all_tests_passed = False
except AssertionError as e:
    print(f"✗ FAIL: {e}")
    all_tests_passed = False

print("\n" + "=" * 60)
print("TEST 7: print() uses __str__() automatically")
print("=" * 60)
try:
    print("\nCalling print(champ1):")
    print(champ1)

    print("\nIf you see the format '{summoner} playing {champion} ({role}) - Level {level}', __str__ works!")
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
    print("\nCongratulations! You've completed all three exercises!")
    print("\nYou now understand:")
    print("  - Instance methods: for champion-specific operations")
    print("  - Class methods: for game-wide statistics and data")
    print("  - Static methods: for utility functions")
    print("  - Magic methods: for customizing Python behavior")
    print("\nYou have a fully-featured Champion class with all method types!")
    print("\n󰟟 Captain Teemo on duty!")
    print("""
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@*:-=++++++-=*@@@@@@@@@@@@@@@@@@@@@@
@@@@@#-:----++++-@@@@@@#+*+**@@@@@@@@@
@@@@@@=-+----:-=-==+*#=%*-=++%@@@@@@@@
@@@%#*+=--::-++++++++++=:::-:-+@@@@@@@
@@*#+----===+==-::::-:--::---:-+@@@@@@
@@@=*-*##+:--:::=+:-===---=-----=+%@@@
@@@#*#=##:---====--::::::-:::::::::=@@
@@@@*--:--:---:::::::----::::--::::+@@
@@@@@#:---::::::::::-+**+++++++=-*@@@@
@@@@%--:::--====++++++%%+=-:-==+=@@@@@
@@@+-:.:-*%%*++-..++=+#%#+++++*#%+#%@@
@@@=...:-#%%*=+++++++##=-#%%%%**#%%=%@
@@@@@@=-#%%%##++***#%%%%##*+#%%%%**@@@
@@@@%::=#%%%%###%#***#***##%%%%%#*=*@@
@@@@@@@=:-#%%%%%%%%%%%%%%%%%%%*=#@@@@@
@@@@@@@+:----=*#%%%%%%%%%%%*=::-#@@@@@
@@@@@@@@%-....::::::::::..::-----#@@@@
@@@@@@@@#...:::::::::----------*@@@@@@
@@@@@@@@@@:.-------::------:---@@@@@@@
@@@@@@@@@@%..:-:::-::-:::---@#@@@@@@@@
@@@@@@@@@@@@@@@@@=#@@@@@@@@@@@@@@@@@@@
""")
