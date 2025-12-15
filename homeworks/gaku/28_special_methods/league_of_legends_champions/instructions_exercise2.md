# Exercise 2: Statistics Methods (Class Methods)

**Read first:** `../lecture/class_methods.md`

**Prerequisites:** Complete Exercise 1 first

## Helpful Hints

### String Formatting
String formatting allows you to control how numbers appear in output strings.

- `f"{value:,}"` - Adds thousand separators
  - Example: `f"{1000:,}"` → `"1,000"`
  - Example: `f"{1234567:,}"` → `"1,234,567"`
- `f"{value:.2f}"` - Formats to 2 decimal places
  - Example: `f"{5.5:.2f}"` → `"5.50"`
  - Example: `f"{3.14159:.2f}"` → `"3.14"`

### Understanding `sum()`
The `sum()` function adds up all values in a list.

**Basic usage:**
- Example: `sum([1, 2, 3])` returns `6`
- Example: `sum([10, 20, 30])` returns `60`

### New Concept: Generator Functions

**What is a generator function?**
A generator function is a compact way to create values on-the-fly as you loop through a collection. Instead of creating a full list first, it generates each value one at a time.

**Using `sum()` with a generator function:**
You can combine `sum()` with a generator function to add up specific values from objects in a list:

- Syntax: `sum(c.level for c in champions)`
- This is called a generator function - it loops through `champions` and generates each champion's `level` value
- The long way to write this would be:
  ```python
  total = 0
  for c in champions:
      total += c.level
  ```
- The `sum()` with generator function does the same thing but in one line
- Pattern: `sum(item.property for item in list)` gets the total of that property from all items

## Task

Add class methods to track game-wide statistics in `hw_class_methods_game_starter.py`.

**Why class methods?** These methods work with class-level data (like `total_champions` and `total_mastery_points`) that's shared across all instances. They need `cls` to access class variables.

## Steps to Complete

**Add these 4 methods in the "EXERCISE 2: CLASS METHODS" section of the file.**

### Step 1: **`get_champion_count(cls)`** - Class method
   - Returns: `"Total champions in game: {count}"`
   - Use the `total_champions` class variable to get the count

### Step 2: **`get_total_mastery(cls)`** - Class method
   - Returns: `"Total mastery points earned: {points}"`
   - Use the `total_mastery_points` class variable
   - Format the points with comma separators using `f"{cls.total_mastery_points:,}"`

### Step 3: **`get_average_level(cls, champions)`** - Class method
   - Takes: list of champion objects
   - Returns: `"Average champion level: {avg}"` formatted with 2 decimal places
   - Calculate average by dividing the sum of all champion levels by the number of champions
   - Use `sum()` with a generator function to get the total of all levels `(see "New Concept: Generator Functions" at top)`
   - Divide the total by the number of champions to get the average
   - If the list is empty, return `"No champions to calculate average"`

### Step 4: **`get_highest_level(cls, champions)`** - Class method
   - Takes: list of champion objects
   - Returns: `"Highest level: {name} (Level {level})"`
   - Use the `find_highest_level_champion()` static method from Exercise 1 to find the champion
   - If the list is empty, return `"No champions found"`

## Test

```bash
python3 test_exercise2.py
```
