#!/usr/bin/env python3
# Test file for Nested Class Exercise - Mario Kart Cup

from mario_kart_cup import Cup

all_tests_passed = True
flower_cup = None

print("=" * 60)
print("MARIO KART CUP - NESTED CLASS TEST")
print("=" * 60)

print("\n" + "=" * 60)
print("TEST 1: Creating a Cup")
print("=" * 60)
try:
    flower_cup = Cup("Flower Cup")
    if hasattr(flower_cup, 'cup_name') and flower_cup.cup_name == "Flower Cup":
        print(f"✓ PASS - Cup created: {flower_cup.cup_name}")
    else:
        print("✗ FAIL - Cup name not stored correctly")
        all_tests_passed = False

    if hasattr(flower_cup, 'racers') and isinstance(flower_cup.racers, list):
        print("✓ PASS - Racers list initialized")
    else:
        print("✗ FAIL - Racers list not initialized")
        all_tests_passed = False
except Exception as e:
    print(f"✗ FAIL - Error creating Cup: {e}")
    all_tests_passed = False

print("\n" + "=" * 60)
print("TEST 2: Adding Racers (Nested Class)")
print("=" * 60)
if flower_cup is None:
    print("✗ FAIL - Cannot run test, Cup was not created in TEST 1")
    all_tests_passed = False
else:
    try:
        result1 = flower_cup.add_racer("Yoshi", "Egg 1")
        result2 = flower_cup.add_racer("Toad", "Toadette Kart")

        expected1 = "Yoshi joined Flower Cup!"
        expected2 = "Toad joined Flower Cup!"

        if result1 == expected1:
            print(f"✓ PASS - {result1}")
        else:
            print(f"✗ FAIL - Expected: '{expected1}', got: '{result1}'")
            all_tests_passed = False

        if result2 == expected2:
            print(f"✓ PASS - {result2}")
        else:
            print(f"✗ FAIL - Expected: '{expected2}', got: '{result2}'")
            all_tests_passed = False

        if len(flower_cup.racers) == 2:
            print(f"✓ PASS - 2 racers added to cup")
        else:
            print(f"✗ FAIL - Expected 2 racers, found {len(flower_cup.racers)}")
            all_tests_passed = False
    except Exception as e:
        print(f"✗ FAIL - Error adding racers: {e}")
        all_tests_passed = False

print("\n" + "=" * 60)
print("TEST 3: Racer Class Attributes")
print("=" * 60)
if flower_cup is None or not hasattr(flower_cup, 'racers') or len(flower_cup.racers) == 0:
    print("✗ FAIL - Cannot run test, no racers added")
    all_tests_passed = False
else:
    try:
        racer = flower_cup.racers[0]

        if hasattr(racer, 'name') and racer.name == "Yoshi":
            print(f"✓ PASS - Racer name: {racer.name}")
        else:
            print(f"✗ FAIL - Racer name not stored correctly")
            all_tests_passed = False

        if hasattr(racer, 'kart') and racer.kart == "Egg 1":
            print(f"✓ PASS - Racer kart: {racer.kart}")
        else:
            print(f"✗ FAIL - Racer kart not stored correctly")
            all_tests_passed = False

        if hasattr(racer, 'points') and racer.points == 0:
            print(f"✓ PASS - Points initialized to 0")
        else:
            print(f"✗ FAIL - Points not initialized to 0")
            all_tests_passed = False
    except Exception as e:
        print(f"✗ FAIL - Error accessing racer attributes: {e}")
        all_tests_passed = False

print("\n" + "=" * 60)
print("TEST 4: Awarding Points")
print("=" * 60)
if flower_cup is None:
    print("✗ FAIL - Cannot run test, Cup was not created")
    all_tests_passed = False
else:
    try:
        result1 = flower_cup.award_points("Yoshi", 15)
        result2 = flower_cup.award_points("Toad", 12)

        expected1 = "Yoshi earned 15 points!"
        expected2 = "Toad earned 12 points!"

        if result1 == expected1:
            print(f"✓ PASS - {result1}")
        else:
            print(f"✗ FAIL - Expected: '{expected1}', got: '{result1}'")
            all_tests_passed = False

        if result2 == expected2:
            print(f"✓ PASS - {result2}")
        else:
            print(f"✗ FAIL - Expected: '{expected2}', got: '{result2}'")
            all_tests_passed = False

        if flower_cup.racers[0].points == 15:
            print(f"✓ PASS - Yoshi has 15 points")
        else:
            print(f"✗ FAIL - Yoshi should have 15 points, has {flower_cup.racers[0].points}")
            all_tests_passed = False
    except Exception as e:
        print(f"✗ FAIL - Error awarding points: {e}")
        all_tests_passed = False

print("\n" + "=" * 60)
print("TEST 5: Award Points - Racer Not Found")
print("=" * 60)
if flower_cup is None:
    print("✗ FAIL - Cannot run test, Cup was not created")
    all_tests_passed = False
else:
    try:
        result = flower_cup.award_points("Wario", 10)
        expected = "Racer Wario not found!"

        if result == expected:
            print(f"✓ PASS - {result}")
        else:
            print(f"✗ FAIL - Expected: '{expected}', got: '{result}'")
            all_tests_passed = False
    except Exception as e:
        print(f"✗ FAIL - Error handling missing racer: {e}")
        all_tests_passed = False

print("\n" + "=" * 60)
print("TEST 6: Racer get_info() Method")
print("=" * 60)
if flower_cup is None:
    print("✗ FAIL - Cannot run test, Cup was not created")
    all_tests_passed = False
else:
    try:
        racer_info = flower_cup.racers[0].get_info()
        expected = "Yoshi (Egg 1) - 15 points"

        if racer_info == expected:
            print(f"✓ PASS - {racer_info}")
        else:
            print(f"✗ FAIL - Expected: '{expected}', got: '{racer_info}'")
            all_tests_passed = False
    except Exception as e:
        print(f"✗ FAIL - Error getting racer info: {e}")
        all_tests_passed = False

print("\n" + "=" * 60)
print("TEST 7: Get All Racers")
print("=" * 60)
if flower_cup is None:
    print("✗ FAIL - Cannot run test, Cup was not created")
    all_tests_passed = False
else:
    try:
        all_racers = flower_cup.get_all_racers()

        if len(all_racers) == 2:
            print(f"✓ PASS - 2 racers in list")
        else:
            print(f"✗ FAIL - Expected 2 racers, got {len(all_racers)}")
            all_tests_passed = False

        expected_racers = [
            "Yoshi (Egg 1) - 15 points",
            "Toad (Toadette Kart) - 12 points"
        ]

        for i, expected in enumerate(expected_racers):
            if all_racers[i] == expected:
                print(f"✓ PASS - Racer {i+1}: {all_racers[i]}")
            else:
                print(f"✗ FAIL - Expected '{expected}', got '{all_racers[i]}'")
                all_tests_passed = False
    except Exception as e:
        print(f"✗ FAIL - Error getting all racers: {e}")
        all_tests_passed = False

print("\n" + "=" * 60)
print("TEST 8: Get Racer Points")
print("=" * 60)
if flower_cup is None:
    print("✗ FAIL - Cannot run test, Cup was not created")
    all_tests_passed = False
else:
    try:
        yoshi_points = flower_cup.get_racer_points("Yoshi")
        toad_points = flower_cup.get_racer_points("Toad")
        wario_points = flower_cup.get_racer_points("Wario")

        if yoshi_points == 15:
            print(f"✓ PASS - Yoshi has {yoshi_points} points")
        else:
            print(f"✗ FAIL - Expected Yoshi to have 15 points, got {yoshi_points}")
            all_tests_passed = False

        if toad_points == 12:
            print(f"✓ PASS - Toad has {toad_points} points")
        else:
            print(f"✗ FAIL - Expected Toad to have 12 points, got {toad_points}")
            all_tests_passed = False

        if wario_points == 0:
            print(f"✓ PASS - Wario not found, returns 0")
        else:
            print(f"✗ FAIL - Expected 0 for non-existent racer, got {wario_points}")
            all_tests_passed = False
    except Exception as e:
        print(f"✗ FAIL - Error getting racer points: {e}")
        all_tests_passed = False

print("\n" + "=" * 60)
print("TEST 9: Get Total Racers")
print("=" * 60)
if flower_cup is None:
    print("✗ FAIL - Cannot run test, Cup was not created")
    all_tests_passed = False
else:
    try:
        total = flower_cup.get_total_racers()

        if total == 2:
            print(f"✓ PASS - Total racers: {total}")
        else:
            print(f"✗ FAIL - Expected 2 racers, got {total}")
            all_tests_passed = False

        # Test with empty cup
        empty_cup = Cup("Star Cup")
        empty_total = empty_cup.get_total_racers()

        if empty_total == 0:
            print(f"✓ PASS - Empty cup has 0 racers")
        else:
            print(f"✗ FAIL - Expected 0 racers in empty cup, got {empty_total}")
            all_tests_passed = False
    except Exception as e:
        print(f"✗ FAIL - Error getting total racers: {e}")
        all_tests_passed = False

print("\n" + "=" * 60)
if all_tests_passed:
    print("ALL TESTS PASSED!")
else:
    print("SOME TESTS FAILED - Fix the errors above and try again")
print("=" * 60)

if all_tests_passed:
    print("\nCongratulations! You've mastered nested classes!")
    print("\nYou now understand:")
    print("  - How to create a class inside another class")
    print("  - How to access nested classes using self.NestedClass")
    print("  - Why nested classes help organize related code")
    print("  - How to use nested classes in real-world scenarios")
    print("\nYou're ready to race in the Mushroom Kingdom!")
    print("\nWahoo! You're egg-cellent at nested classes! Yoshi approves!")
    print("""
@%@%@%%@%@%@%@%@@@@@@@#*#@@@@%@%@@%@%@%@
@%@%@%@@%@%@%@#.:--..-====.-@@@%@@%@%@%@
@%@%@%@@%@%@@=.+@%=.+%@@====.#@%@@%@%@%@
@%@%@%@@@@@@*.%@@@#@@@@@@%===.#@@@%@%@%@
%@%@%@@%@%@@.+@-.%@*.=@@@@===:=@@@@%@%@%
%@%@%@@@@#+=.#@..%@  .@@@@#===....*@@%@%
%@@@@:.:=======-.:@= -@@@@%-==-.++.#@%@%
@@%..==============:%@@@@@*====-.+:+@@%@
@#.-==:==:==========-**=-=======-..%@@%@
%.-=========================-====--..+@@
=:=======================-%@@@@@@@%.-=.#
-:=====================-#@@@@@@@@@@*.+:=
=:=====================%@@@@@@@@@@@*.-.@
%.-===================-@@@@@@@@@@@@..=@@
@#.-=================:+@@@@@@@@@@@- %@%@
@@%::==============-:%#*@@@@@@@@*.-.#@%@
@%@@%-.:-=====-:..+@@@@@@@@@@%-.-=::@@%@
@%@%@@@@%#***##:.-=++*@@%+-...=##%@@@@@@
@@@@@@@@@@%@@@@@@@+.@@@@*==.=@%..:::..#@
    """)
