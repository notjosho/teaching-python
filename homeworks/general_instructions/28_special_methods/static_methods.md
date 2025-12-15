# Static Methods

## What Are They?

Static methods are utility functions that belong to a class but don't need access to instance or class data.

## Syntax

```python
class MyClass:
    @staticmethod
    def add_numbers(a, b):
        return a + b
```

**Key points:**
- Use `@staticmethod` decorator
- No `self` or `cls` parameter
- Cannot access instance or class variables
- Just regular functions organized in a class
- Can be called on class: `MyClass.add_numbers(5, 3)`

## When to Use

Use static methods for:
1. **Validation functions** (check if input is valid)
2. **Formatting functions** (format data)
3. **Calculations** (math or business logic)
4. **Utility helpers** related to the class

## Examples

### Example 1: Validation
```python
class Email:
    def __init__(self, address):
        if not Email.is_valid(address):
            raise ValueError("Invalid email")
        self.address = address

    @staticmethod
    def is_valid(email):
        return '@' in email and '.' in email.split('@')[1]

# Usage
print(Email.is_valid("test@example.com"))  # True
print(Email.is_valid("invalid"))            # False
email = Email("user@example.com")
```

### Example 2: Formatting
```python
class TextFormatter:
    @staticmethod
    def format_title(text):
        return text.title()

    @staticmethod
    def format_percentage(value):
        return f"{value:.1f}%"

# Usage
print(TextFormatter.format_title("hello world"))  # Hello World
print(TextFormatter.format_percentage(25.5))       # 25.5%
```

### Example 3: Calculations
```python
class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(celsius):
        return (celsius * 9/5) + 32

    @staticmethod
    def fahrenheit_to_celsius(fahrenheit):
        return (fahrenheit - 32) * 5/9

# Usage
temp_f = TemperatureConverter.celsius_to_fahrenheit(100)  # 212.0
temp_c = TemperatureConverter.fahrenheit_to_celsius(32)   # 0.0
```

### Example 4: Generating IDs
```python
import random

class IDGenerator:
    @staticmethod
    def generate_code():
        return f"CODE{random.randint(1000, 9999)}"

# Usage
print(IDGenerator.generate_code())  # CODE5847
```

## Instance vs Class vs Static

| Type | First Param | Access Instance Data | Access Class Data | Use For |
|------|-------------|---------------------|-------------------|---------|
| Instance | `self` | Yes | Yes | Operations on one object |
| Class | `cls` | No | Yes | Operations on class data |
| Static | None | No | No | Utility functions |

## When NOT to Use

❌ **Don't use if you need instance data:**
```python
class Bad:
    def __init__(self, name):
        self.name = name

    @staticmethod
    def get_name():  # Can't access self.name!
        pass
```

✅ **Use instance method instead:**
```python
class Good:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name
```

❌ **Don't use if you need class data:**
```python
class Bad:
    count = 0

    @staticmethod
    def get_count():  # Can't access count!
        pass
```

✅ **Use class method instead:**
```python
class Good:
    count = 0

    @classmethod
    def get_count(cls):
        return cls.count
```

## Summary

- Static methods are **utility functions** in a class
- Use `@staticmethod`, no `self` or `cls`
- Perfect for **validation**, **formatting**, **calculations**
- Cannot access instance or class data
- Called on the class: `MyClass.method()`
