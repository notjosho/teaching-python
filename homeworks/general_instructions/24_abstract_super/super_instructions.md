# Using super() in Python Inheritance

## Instructions

Create a file called `super.py` with the following:

1. Create a class called `Animal`:
   - The constructor should accept `name` and `age` as parameters and store them as instance attributes
   - Set an instance attribute `energy` to 100
   - Add a method called `speak()` that returns the string "Some generic sound"
   - Add a method called `info()` that returns a string in the format "{name} is {age} years old"
   - Add a method called `eat()` that increases energy by 20 (max 100) and returns the energy value
   - Add a method called `play()` that decreases energy by 15 (min 0) and returns the energy value

2. Create a class called `Dog` that inherits from `Animal`:
   - The constructor should accept `name`, `age`, and `breed` as parameters
   - Use `super` to call the parent constructor
   - Store `breed` as an instance attribute
   - Override the `speak()` method to:
     - Use `super` to get the parent's result
     - Return a string in the format "{parent_sound} - but actually: Woof! Woof!"
   - Override the `info()` method to:
     - Use `super` to get the parent's result
     - Return a string in the format "{parent_info} and is a {breed}"

3. Create a class called `Cat` that inherits from `Animal`:
   - The constructor should accept `name`, `age`, and `color` as parameters
   - Use `super` to call the parent constructor
   - Store `color` as an instance attribute
   - Override the `speak()` method to return the string "Meow!"
   - Override the `info()` method to:
     - Use `super` to get the parent's result
     - Return a string in the format "{parent_info} and has {color} fur"

4. Create a class called `Bird` that inherits from `Animal`:
   - The constructor should accept `name`, `age`, and `species` as parameters
   - Use `super` to call the parent constructor
   - Store `species` as an instance attribute
   - Set an instance attribute `flight_distance` to 0
   - Override the `speak()` method to return the string "Chirp chirp!"
   - Override the `info()` method to:
     - Use `super` to get the parent's result
     - Return a string in the format "{parent_info}, is a {species}, and has flown {flight_distance} km"
   - Override the `eat()` method to:
     - Use `super` to call the parent's eat method (this returns the updated energy)
     - Add an additional 10 to the energy attribute
     - If energy exceeds 100, set it to 100
     - Return the energy value
   - Override the `play()` method to:
     - Use `super` to call the parent's play method (this returns the updated energy)
     - Add 5 to the flight_distance attribute
     - Decrease the energy attribute by an additional 5
     - If energy goes below 0, set it to 0
     - Return the energy value

**Note:** You can optionally add code at the bottom to create instances and print results for manual testing, but this is not required since the test file will verify your implementation.

## Testing

Run the test file to verify your implementation:
```bash
python3 test_super.py
```
