#!/usr/bin/env python3
# Test file for Exercise 1: Static Methods

from hw_class_methods_game import Champion

all_tests_passed = True

print("=" * 60)
print("EXERCISE 1: STATIC METHODS TEST - League of Legends")
print("=" * 60)

print("\n" + "=" * 60)
print("STEP 1: Testing validate_summoner_name()")
print("=" * 60)
print("\n" + "=" * 60)
print("TEST 1: validate_summoner_name() - valid names")
print("=" * 60)
try:
    test_cases = [
        ("Faker", True),
        ("TheShy", True),
        ("CoreJJ", True),
        ("Uzi123", True),
    ]

    all_passed = True
    for name, expected in test_cases:
        result = Champion.validate_summoner_name(name)
        status = "✓" if result == expected else "✗"
        print(f"{status} validate_summoner_name('{name}') = {result} (expected {expected})")
        if result != expected:
            all_passed = False

    if all_passed:
        print("✓ PASS - All valid summoner names accepted")
    else:
        print("✗ FAIL - Some valid names rejected")
        all_tests_passed = False
except AttributeError:
    print("✗ FAIL: Method validate_summoner_name() not implemented")
    all_tests_passed = False

print("\n" + "=" * 60)
print("TEST 2: validate_summoner_name() - invalid names")
print("=" * 60)
try:
    test_cases = [
        ("AB", False),  # Too short
        ("NameThatIsTooLongForLoL", False),  # Too long
        ("Name-With-Dash", False),  # Contains dashes
        ("", False),  # Empty
    ]

    all_passed = True
    for name, expected in test_cases:
        result = Champion.validate_summoner_name(name)
        status = "✓" if result == expected else "✗"
        print(f"{status} validate_summoner_name('{name}') = {result} (expected {expected})")
        if result != expected:
            all_passed = False

    if all_passed:
        print("✓ PASS - All invalid summoner names rejected")
    else:
        print("✗ FAIL - Some invalid names accepted")
        all_tests_passed = False
except AttributeError:
    print("✗ FAIL: Method validate_summoner_name() not implemented")
    all_tests_passed = False

print("\n" + "=" * 60)
print("STEP 2: Testing is_valid_role()")
print("=" * 60)
print("\n" + "=" * 60)
print("TEST 3: is_valid_role() - valid roles")
print("=" * 60)
try:
    test_cases = [
        ("Top", True),
        ("Jungle", True),
        ("Mid", True),
        ("ADC", True),
        ("Support", True),
    ]

    all_passed = True
    for role, expected in test_cases:
        result = Champion.is_valid_role(role)
        status = "✓" if result == expected else "✗"
        print(f"{status} is_valid_role('{role}') = {result} (expected {expected})")
        if result != expected:
            all_passed = False

    if all_passed:
        print("✓ PASS - All valid roles accepted")
    else:
        print("✗ FAIL - Some valid roles rejected")
        all_tests_passed = False
except AttributeError:
    print("✗ FAIL: Method is_valid_role() not implemented")
    all_tests_passed = False

print("\n" + "=" * 60)
print("TEST 4: is_valid_role() - invalid roles")
print("=" * 60)
try:
    test_cases = [
        ("Carry", False),
        ("Tank", False),
        ("mid", False),  # Wrong case
        ("", False),
    ]

    all_passed = True
    for role, expected in test_cases:
        result = Champion.is_valid_role(role)
        status = "✓" if result == expected else "✗"
        print(f"{status} is_valid_role('{role}') = {result} (expected {expected})")
        if result != expected:
            all_passed = False

    if all_passed:
        print("✓ PASS - All invalid roles rejected")
    else:
        print("✗ FAIL - Some invalid roles accepted")
        all_tests_passed = False
except AttributeError:
    print("✗ FAIL: Method is_valid_role() not implemented")
    all_tests_passed = False

print("\n" + "=" * 60)
print("STEP 3: Testing calculate_damage()")
print("=" * 60)
print("\n" + "=" * 60)
print("TEST 5: calculate_damage() - damage calculation")
print("=" * 60)
try:
    # Test damage scaling with level
    damage1 = Champion.calculate_damage(50, 1)
    damage5 = Champion.calculate_damage(50, 5)
    damage10 = Champion.calculate_damage(50, 10)

    print(f"Level 1 damage: {damage1} (base 50)")
    print(f"Level 5 damage: {damage5} (should be higher)")
    print(f"Level 10 damage: {damage10} (should be even higher)")

    if damage1 < damage5 < damage10:
        print("✓ PASS - Damage scales with level")
    else:
        print("✗ FAIL - Damage doesn't scale properly")
        all_tests_passed = False
except AttributeError:
    print("✗ FAIL: Method calculate_damage() not implemented")
    all_tests_passed = False

print("\n" + "=" * 60)
print("STEP 4: Testing generate_summoner_id()")
print("=" * 60)
print("\n" + "=" * 60)
print("TEST 6: generate_summoner_id() - ID format")
print("=" * 60)
try:
    ids = [Champion.generate_summoner_id() for _ in range(5)]
    print(f"Generated IDs: {ids}")

    all_valid = all(
        id.startswith('S') and len(id) == 5 and id[1:].isdigit()
        for id in ids
    )

    if all_valid:
        print("✓ PASS - All IDs have correct format (S + 4 digits)")
    else:
        print("✗ FAIL - Some IDs have incorrect format")
        all_tests_passed = False
except AttributeError:
    print("✗ FAIL: Method generate_summoner_id() not implemented")
    all_tests_passed = False

print("\n" + "=" * 60)
print("TEST 7: generate_summoner_id() - uniqueness check")
print("=" * 60)
try:
    ids = [Champion.generate_summoner_id() for _ in range(100)]
    unique_count = len(set(ids))

    print(f"Generated 100 IDs, {unique_count} unique")

    # At least 90% should be unique (allowing for some random collisions)
    if unique_count >= 90:
        print("✓ PASS - IDs are sufficiently random")
    else:
        print("✗ FAIL - Not enough unique IDs generated")
        all_tests_passed = False
except AttributeError:
    print("✗ FAIL: Method generate_summoner_id() not implemented")
    all_tests_passed = False

print("\n" + "=" * 60)
print("STEP 5: Testing find_highest_level_champion()")
print("=" * 60)
print("\n" + "=" * 60)
print("TEST 8: find_highest_level_champion() - finding highest level")
print("=" * 60)
try:
    # Create test champions with different levels
    champ1 = Champion("Faker", "Zed", "Mid")
    champ2 = Champion("TheShy", "Yasuo", "Top")
    champ3 = Champion("Uzi", "Vayne", "ADC")

    # Level them up to different levels
    champ1.level = 5
    champ2.level = 10
    champ3.level = 3

    champions = [champ1, champ2, champ3]
    highest = Champion.find_highest_level_champion(champions)

    print(f"Champions: {champ1.champion_name} (Lv{champ1.level}), {champ2.champion_name} (Lv{champ2.level}), {champ3.champion_name} (Lv{champ3.level})")
    print(f"Highest: {highest.champion_name} (Lv{highest.level})")

    if highest is champ2:
        print("✓ PASS - Correctly found highest level champion")
    else:
        print(f"✗ FAIL - Should find {champ2.champion_name} but found {highest.champion_name}")
        all_tests_passed = False
except AttributeError:
    print("✗ FAIL: Method find_highest_level_champion() not implemented")
    all_tests_passed = False
except Exception as e:
    print(f"✗ FAIL: {e}")
    all_tests_passed = False

print("\n" + "=" * 60)
print("TEST 9: find_highest_level_champion() - empty list handling")
print("=" * 60)
try:
    try:
        result = Champion.find_highest_level_champion([])
        print("✗ FAIL - Should handle empty list gracefully or raise informative error")
        all_tests_passed = False
    except IndexError:
        print("⚠ WARNING - Method crashes on empty list with IndexError")
        print("  Recommendation: Add error handling to check if list is empty")
        print("  For now, students should avoid passing empty lists")
        # Don't fail the test for this - it's just a warning
except AttributeError:
    print("✗ FAIL: Method find_highest_level_champion() not implemented")
    all_tests_passed = False

print("\n" + "=" * 60)
print("STEP 6-7: Testing __init__() validation")
print("=" * 60)
print("\n" + "=" * 60)
print("TEST 10: __init__() validation - invalid summoner name")
print("=" * 60)
try:
    # Test too short
    try:
        champ = Champion("AB", "Zed", "Mid")
        print("✗ FAIL - Should reject summoner name 'AB' (too short)")
        all_tests_passed = False
    except ValueError as e:
        if "Invalid summoner name" in str(e):
            print(f"✓ PASS - Rejected 'AB': {e}")
        else:
            print(f"✗ FAIL - Wrong error message: {e}")
            all_tests_passed = False

    # Test too long
    try:
        champ = Champion("NameThatIsTooLong", "Zed", "Mid")
        print("✗ FAIL - Should reject summoner name (too long)")
        all_tests_passed = False
    except ValueError as e:
        if "Invalid summoner name" in str(e):
            print(f"✓ PASS - Rejected long name: {e}")
        else:
            print(f"✗ FAIL - Wrong error message: {e}")
            all_tests_passed = False

    # Test special characters
    try:
        champ = Champion("Name-123", "Zed", "Mid")
        print("✗ FAIL - Should reject summoner name with special characters")
        all_tests_passed = False
    except ValueError as e:
        if "Invalid summoner name" in str(e):
            print(f"✓ PASS - Rejected 'Name-123': {e}")
        else:
            print(f"✗ FAIL - Wrong error message: {e}")
            all_tests_passed = False

except Exception as e:
    print(f"✗ FAIL: Validation not implemented properly - {e}")
    all_tests_passed = False

print("\n" + "=" * 60)
print("TEST 11: __init__() validation - invalid role")
print("=" * 60)
try:
    # Test invalid role
    try:
        champ = Champion("Faker", "Zed", "Carry")
        print("✗ FAIL - Should reject invalid role 'Carry'")
        all_tests_passed = False
    except ValueError as e:
        if "Invalid role" in str(e):
            print(f"✓ PASS - Rejected 'Carry': {e}")
        else:
            print(f"✗ FAIL - Wrong error message: {e}")
            all_tests_passed = False

    # Test wrong case
    try:
        champ = Champion("Faker", "Zed", "mid")
        print("✗ FAIL - Should reject role 'mid' (wrong case)")
        all_tests_passed = False
    except ValueError as e:
        if "Invalid role" in str(e):
            print(f"✓ PASS - Rejected 'mid': {e}")
        else:
            print(f"✗ FAIL - Wrong error message: {e}")
            all_tests_passed = False

except Exception as e:
    print(f"✗ FAIL: Validation not implemented properly - {e}")
    all_tests_passed = False

print("\n" + "=" * 60)
print("TEST 12: __init__() validation - valid data accepted")
print("=" * 60)
try:
    champ = Champion("Faker", "Zed", "Mid")
    print(f"✓ PASS - Created champion: {champ.summoner_name}'s {champ.champion_name} ({champ.role})")
except Exception as e:
    print(f"✗ FAIL: Valid data should be accepted - {e}")
    all_tests_passed = False

print("\n" + "=" * 60)
if all_tests_passed:
    print("EXERCISE 1 COMPLETE!")
else:
    print("EXERCISE 1 FAILED - Fix the errors above and try again")
print("=" * 60)
