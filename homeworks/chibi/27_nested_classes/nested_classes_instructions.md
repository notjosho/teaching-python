# Nested Class Exercise: Mario Kart Cup

Think of a **Cup** (tournament) in Mario Kart. A Cup has multiple **Racers**, but those racers only exist within the context of that specific cup.

```
Cup (Outer Class)
├── Racer (Inner/Nested Class)
├── Racer (Inner/Nested Class)
└── Racer (Inner/Nested Class)
```

## Your Task

Create a new file called `mario_kart_cup.py` and build a nested class system from scratch.

**Start with an empty file and follow the steps below to build your solution.**

### The Structure

```python
class Cup:                    # Outer class
    class Racer:             # Nested class
        # Racer methods

    # Cup methods that use Racer
```

## Steps to Complete

### Step 1: Create the Cup Class and Nested Racer Class

Start by creating the outer `Cup` class with a nested `Racer` class inside it.

**For the nested `Racer` class, create these methods:**

**`__init__(self, name, kart)`**
- Store the racer's `name`
- Store the racer's `kart`
- Initialize `points` to 0

**`add_points(self, points)`**
- Add the given points to `self.points`

**`get_info(self)`**
- Return: `"{name} ({kart}) - {points} points"`
- Example: `"Mario (Standard Kart) - 39 points"`

### Step 2: Add Methods to the Cup Class

**For the outer `Cup` class, create these methods:**

**`__init__(self, cup_name)`**
- Store the `cup_name`
- Create an empty list called `racers`

**`add_racer(self, name, kart)`**
- Create a new `Racer` using `self.Racer(name, kart)`
  - Note: Access the nested class with `self.Racer`
- Add the racer to `self.racers`
- Return: `"{name} joined {cup_name}!"`

**`award_points(self, racer_name, points)`**
- Loop through `self.racers`
- Find the racer whose name matches `racer_name`
- Call that racer's `add_points(points)` method
- Return: `"{racer_name} earned {points} points!"`
- If racer not found, return: `"Racer {racer_name} not found!"`

**`get_all_racers(self)`**
- Create an empty list called `racer_list`
- Loop through `self.racers`
- Append each racer's `get_info()` to the list
- Return the `racer_list`

**`get_racer_points(self, racer_name)`**
- Loop through `self.racers`
- Find the racer whose name matches `racer_name`
- Return that racer's `points`
- If racer not found, return `0`

**`get_total_racers(self)`**
- Return the length of `self.racers`
  - Hint: Use `len()`

## Key Concept: Accessing Nested Classes

To create an instance of the nested class from inside the outer class:

```python
new_racer = self.Racer(name, kart)  # Use self.Racer
```

To access it from outside:

```python
cup = Cup("Mushroom Cup")
racer = cup.Racer("Mario", "Standard Kart")  # Use instance.Racer
```

## Test Your Code

```bash
python3 test_mario_kart.py
```

## Hints

- The nested `Racer` class is accessed using `self.Racer` inside the `Cup` class
- Use `for` loops to iterate through `self.racers`
- To build lists, use: `for racer in self.racers: racer_list.append(racer.get_info())`
- String formatting: Use f-strings like `f"{name} ({kart}) - {points} points"`
- Use `len(self.racers)` to get the total number of racers

## Why Nested Classes?

This design makes sense because:
- A `Racer` only exists in the context of a `Cup`
- It keeps `Cup` and `Racer` tightly coupled
- It prevents naming conflicts (another program might have a different `Racer` class)
- It shows clear ownership: "A Cup has Racers"
