# Abstract Base Classes Exercise

## Instructions

Create a file called `abstract.py` with the following:

1. Import `ABC` and `abstractmethod` from the `abc` module

2. Create an abstract class called `Shape` that inherits from `ABC`:
   - Add an abstract method called `area()` that takes no parameters (besides self)
     - Use the `@abstractmethod` decorator
     - The method body should only contain `pass`
   - Add an abstract method called `perimeter()` that takes no parameters (besides self)
     - Use the `@abstractmethod` decorator
     - The method body should only contain `pass`

3. Create a class called `Rectangle` that inherits from `Shape`:
   - The constructor should accept `width` and `height` as parameters and store them as instance attributes
   - Implement the `area()` method to return width multiplied by height
   - Implement the `perimeter()` method to return 2 times (width plus height)

4. Create a class called `Circle` that inherits from `Shape`:
   - The constructor should accept `radius` as a parameter and store it as an instance attribute
   - Implement the `area()` method to return 3.14 multiplied by radius squared
   - Implement the `perimeter()` method to return 2 multiplied by 3.14 multiplied by radius

**Note:** You can optionally add code at the bottom to create instances and print results for manual testing, but this is not required since the test file will verify your implementation.

## Testing

Run the test file to verify your implementation:
```bash
python3 test_abstract.py
```
