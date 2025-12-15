# Exercise 3: Magic Methods

**Read first:** `../lecture/magic_methods.md`

## Task

Add magic methods to the `Champion` class in `hw_class_methods_game_starter.py`:

**Why magic methods?** These special methods let you customize how Python behaves with your objects - how they're printed, compared, and sorted. Python automatically calls these methods in specific situations.

### Methods to Implement

1. **`__str__(self)`** - Magic method
   - Returns: `"{summoner_name} playing {champion_name} ({role}) - Level {level}"`
   - Example: `"Faker playing Zed (Mid) - Level 18"`

2. **`__repr__(self)`** - Magic method
   - Returns: `"Champion(summoner_name='{name}', champion_name='{champ}', role='{role}', level={level})"`
   - Example: `"Champion(summoner_name='Faker', champion_name='Zed', role='Mid', level=18)"`

3. **`__eq__(self, other)`** - Magic method
   - Returns: `True` if same summoner name (case-insensitive)
   - Hint: `.lower()`

4. **`__lt__(self, other)`** - Magic method
   - Returns: `True` if `self.level < other.level`
   - Enables sorting by level

## Test

```bash
python3 test_exercise3.py
```
