#!/usr/bin/env python3
# Test file for Exercise 2: Class Methods
#
# PREREQUISITE: Complete Exercise 1 first!
# This test assumes Exercise 1's validation methods work correctly.
# If you get ValueError when creating champions, complete Exercise 1 first.

from hw_class_methods_game import Champion

all_tests_passed = True

print("=" * 60)
print("EXERCISE 2: CLASS METHODS TEST - League of Legends")
print("=" * 60)

# Reset class variables for testing
Champion.total_champions = 0
Champion.total_mastery_points = 0

# Create test champions
print("\nCreating test champions...")
champ1 = Champion("Faker", "Zed", "Mid")
champ2 = Champion("TheShy", "Fiora", "Top")
champ3 = Champion("Uzi", "Vayne", "ADC")

# Simulate leveling
champ1.level = 2
champ2.level = 1
champ3.level = 3

# Add some mastery points
champ1.mastery_points = 500
champ2.mastery_points = 200
champ3.mastery_points = 800
Champion.total_mastery_points = 1500

print(f"Created {Champion.total_champions} champions")

print("\n" + "=" * 60)
print("TEST 1: get_champion_count()")
print("=" * 60)
try:
    result = Champion.get_champion_count()
    print(f"Result: {result}")

    assert "Total champions in game: 3" == result, f"Expected 'Total champions in game: 3', got '{result}'"
    print("✓ PASS")
except AttributeError:
    print("✗ FAIL: Method get_champion_count() not implemented")
    all_tests_passed = False
except AssertionError as e:
    print(f"✗ FAIL: {e}")
    all_tests_passed = False

print("\n" + "=" * 60)
print("TEST 2: get_total_mastery()")
print("=" * 60)
try:
    result = Champion.get_total_mastery()
    print(f"Result: {result}")

    assert "Total mastery points earned: 1,500" == result, f"Expected 'Total mastery points earned: 1,500', got '{result}'"
    print("✓ PASS")
except AttributeError:
    print("✗ FAIL: Method get_total_mastery() not implemented")
    all_tests_passed = False
except AssertionError as e:
    print(f"✗ FAIL: {e}")
    all_tests_passed = False

print("\n" + "=" * 60)
print("TEST 3: get_average_level() - with champions")
print("=" * 60)
try:
    all_champs = [champ1, champ2, champ3]
    result = Champion.get_average_level(all_champs)
    print(f"Levels: Faker={champ1.level}, TheShy={champ2.level}, Uzi={champ3.level}")
    print(f"Result: {result}")

    assert "Average champion level: 2.00" == result, f"Expected 'Average champion level: 2.00', got '{result}'"
    print("✓ PASS")
except AttributeError:
    print("✗ FAIL: Method get_average_level() not implemented")
    all_tests_passed = False
except AssertionError as e:
    print(f"✗ FAIL: {e}")
    all_tests_passed = False

print("\n" + "=" * 60)
print("TEST 4: get_average_level() - empty list")
print("=" * 60)
try:
    result = Champion.get_average_level([])
    print(f"Result: {result}")

    assert "No champions to calculate average" == result, f"Expected 'No champions to calculate average', got '{result}'"
    print("✓ PASS")
except AttributeError:
    print("✗ FAIL: Method get_average_level() not implemented")
    all_tests_passed = False
except AssertionError as e:
    print(f"✗ FAIL: {e}")
    all_tests_passed = False

print("\n" + "=" * 60)
print("TEST 5: get_highest_level() - Uzi is highest")
print("=" * 60)
try:
    all_champs = [champ1, champ2, champ3]
    result = Champion.get_highest_level(all_champs)
    print(f"Result: {result}")

    assert "Highest level: Uzi's Vayne (Level 3)" == result, f"Expected 'Highest level: Uzi's Vayne (Level 3)', got '{result}'"
    print("✓ PASS")
except AttributeError:
    print("✗ FAIL: Method get_highest_level() not implemented")
    all_tests_passed = False
except AssertionError as e:
    print(f"✗ FAIL: {e}")
    all_tests_passed = False

print("\n" + "=" * 60)
print("TEST 6: get_highest_level() - empty list")
print("=" * 60)
try:
    result = Champion.get_highest_level([])
    print(f"Result: {result}")

    assert "No champions found" == result, f"Expected 'No champions found', got '{result}'"
    print("✓ PASS")
except AttributeError:
    print("✗ FAIL: Method get_highest_level() not implemented")
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
