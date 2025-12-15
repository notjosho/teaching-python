# Class Methods

## What Are They?

Class methods are methods that work with class-level data (shared across all instances), not individual object data.

## Syntax

```python
class MyClass:
    count = 0  # Class variable (shared)

    @classmethod
    def get_count(cls):
        return cls.count
```

**Key points:**
- Use `@classmethod` decorator
- First parameter is `cls` (the class itself, like `MyClass`)
- `cls()` calls `__init__` to create a new object (same as `MyClass()`)
- Access class variables with `cls.variable`
- Can be called on class: `MyClass.get_count()`

## When to Use

Use class methods when you need to:
1. **Access or modify class variables** (data shared by all instances)
2. **Get statistics** about all instances
3. **Create alternative constructors** (factory methods)

## Examples

### Example 1: Tracking Inventory
```python
class Product:
    total_inventory = 0

    def __init__(self, name, stock):
        self.name = name
        self.stock = stock
        Product.total_inventory += stock

    @classmethod
    def get_total_inventory(cls):
        return f"Total items in stock: {cls.total_inventory}"

# Usage
p1 = Product("Laptop", 10)
p2 = Product("Mouse", 50)
print(Product.get_total_inventory())  # Total items in stock: 60
```

### Example 2: Computing Statistics
```python
class Employee:
    all_employees = []

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.all_employees.append(self)

    @classmethod
    def get_average_salary(cls):
        if not cls.all_employees:
            return 0
        total = sum(e.salary for e in cls.all_employees)
        return total / len(cls.all_employees)

# Usage
e1 = Employee("Alice", 70000)
e2 = Employee("Bob", 60000)
print(Employee.get_average_salary())  # 65000.0
```

### Example 3: Factory Method (Converting Input Formats)

Factory methods are shortcuts that convert one format to another for you.

**The Problem:** You have a string `"2024-12-14"` but `Date()` needs 3 separate numbers.

```python
class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    @classmethod
    def from_string(cls, date_string):
        # Parse the string for the user
        year, month, day = date_string.split('-')
        # cls() calls __init__ to create a new Date object
        # cls(2024, 12, 14) is the same as Date(2024, 12, 14)
        return cls(int(year), int(month), int(day))

# Without factory - you do the parsing:
date_str = "2024-12-14"
parts = date_str.split('-')
date1 = Date(int(parts[0]), int(parts[1]), int(parts[2]))  # Annoying!

# With factory - it does the parsing for you:
date2 = Date.from_string("2024-12-14")  # Easy!
```

**Why it's useful:**
```python
# Reading dates from a file:
dates = ["2024-01-15", "2024-02-20", "2024-03-25"]

# Easy conversion:
for date_str in dates:
    date = Date.from_string(date_str)  # One line!
```

## Instance vs Class vs Static

| Type | First Param | Access Instance Data | Access Class Data | Use For |
|------|-------------|---------------------|-------------------|---------|
| Instance | `self` | Yes | Yes | Operations on one object |
| Class | `cls` | No | Yes | Operations on class data |
| Static | None | No | No | Utility functions |

## Common Mistakes

❌ **Wrong:** Using class name instead of `cls`
```python
@classmethod
def bad_method(cls):
    return MyClass.count  # Don't hardcode class name
```

✅ **Correct:**
```python
@classmethod
def good_method(cls):
    return cls.count  # Use cls
```

## Summary

- Class methods work with **class-level data**
- Use `@classmethod` and `cls` parameter
- Perfect for **statistics** and **factory methods**
- Called on the class: `MyClass.method()`

