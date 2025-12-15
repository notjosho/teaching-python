# Exercise 1: Utility Methods (Static Methods)

**Read first:** `../lecture/static_methods.md`

## Helpful Hints

### Understanding `.isalnum()`
The `.isalnum()` method checks if a string contains only letters and numbers (no spaces or special characters).

- Returns `True` if all characters are alphanumeric
- Returns `False` if there are spaces, dashes, or special characters
- Example: `"Faker123".isalnum()` → `True`
- Example: `"Faker-123".isalnum()` → `False` (has a dash)
- Example: `"Faker 123".isalnum()` → `False` (has a space)

### Understanding `random.randint()`
The `random.randint(a, b)` function returns a random integer between `a` and `b` (inclusive).

- Example: `random.randint(1000, 9999)` returns a random number from 1000 to 9999
- Example: `random.randint(0, 15)` returns a random number from 0 to 15

## Task

Build utility methods for the `Champion` class in `hw_class_methods_game_starter.py`.

These will be used in Exercise 2.

**Why static methods?** These are utility functions that don't need access to instance data (`self`) or class data (`cls`). They're helpers that could work independently but belong with the class logically.

## Steps to Complete

### STEP 1-5: Create Static Methods

**Add these 5 methods in the "EXERCISE 1: STATIC METHODS" section of the file.**

#### Step 1: **`validate_summoner_name(summoner_name)`** - Static method
   - Returns: `True` if valid, `False` otherwise
   - Valid: 3-16 characters, alphanumeric only
   - Hint: Use `len()` to check length and `.isalnum()` to verify the name contains only letters and numbers

#### Step 2: **`is_valid_role(role)`** - Static method
   - Returns: `True` if in `Champion.valid_roles`, `False` otherwise
   - Valid roles: Top, Jungle, Mid, ADC, Support
   - Hint: `in` operator

#### Step 3: **`calculate_damage(base_ad, level)`** - Static method
   - Returns: total attack damage (integer)
   - Formula: `base_ad + (level - 1) * 3 + random.randint(0, 15)`

#### Step 4: **`generate_summoner_id()`** - Static method
   - Returns: `"S"` + 4-digit random number (1000-9999)
   - Example: `"S1234"`
   - Hint: Use `random.randint()` to generate the random number

#### Step 5: **`find_highest_level_champion(champions)`** - Static method
   - Takes: list of champion objects
   - Returns: the champion object with the highest level
   - This will be used in Exercise 2
   - Algorithm approach:
     1. Start with the first champion as the current highest
     2. Loop through all champions in the list
     3. If a champion's level is higher than the current highest level, update the current highest
     4. Return the champion with the highest level

### STEP 6-7: Update Existing Code

**Modify existing methods to use the static methods you created.**

#### Step 6: **Update `__init__()` to use validation**
   - Add validation at the start of `__init__()` before setting attributes
   - Use `validate_summoner_name()` to check the summoner name
   - If invalid, raise: `ValueError("Invalid summoner name. Must be 3-16 characters, alphanumeric only")`
   - Use `is_valid_role()` to check the role
   - If invalid, raise: `ValueError(f"Invalid role. Choose from: {', '.join(Champion.valid_roles)}")`
   - Use `generate_summoner_id()` instead of the inline random code for `self.summoner_id`

#### Step 7: **Update `attack()` method to use `calculate_damage()`**
   - Find the `attack()` method in the "INSTANCE METHODS" section
   - Replace the inline damage calculation with: `Champion.calculate_damage(50, self.level)`

## Test

```bash
python3 test_exercise1.py
```

**Next:** Exercise 2 will use these utilities!
