# Magic Methods (Dunder Methods)

## What Are They?

Magic methods are special methods with double underscores (`__method__`) that Python calls automatically. They let you customize how your objects behave with built-in Python operations.

## Why "Magic"?

You rarely call them directly - Python calls them for you:
- `print(obj)` → calls `obj.__str__()`
- `len(obj)` → calls `obj.__len__()`
- `obj1 == obj2` → calls `obj1.__eq__(obj2)`

## Common Magic Methods

### 1. String Representation

**`__str__(self)`** - User-friendly display
```python
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"'{self.title}' by {self.author}"

book = Book("1984", "Orwell")
print(book)  # '1984' by Orwell
```

**`__repr__(self)`** - Developer-friendly (for debugging)
```python
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __repr__(self):
        return f"Book('{self.title}', '{self.author}')"

book = Book("1984", "Orwell")
print(repr(book))  # Book('1984', 'Orwell')
```

**Difference:**
- `__str__`: For humans, easy to read
- `__repr__`: For developers, shows how to recreate the object

### 2. Comparison Methods

**`__eq__(self, other)`** - Equality (`==`)
```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

p1 = Point(1, 2)
p2 = Point(1, 2)
print(p1 == p2)  # True
```

**`__lt__(self, other)`** - Less than (`<`)
```python
class Movie:
    def __init__(self, title, rating):
        self.title = title
        self.rating = rating

    def __lt__(self, other):
        return self.rating < other.rating

m1 = Movie("Movie A", 7.5)
m2 = Movie("Movie B", 8.5)
print(m1 < m2)  # True

# Enables sorting!
movies = [m2, m1]
sorted_movies = sorted(movies)
print([m.title for m in sorted_movies])  # ['Movie A', 'Movie B']
```

**Other comparison methods:**
- `__le__(self, other)` - Less than or equal (`<=`)
- `__gt__(self, other)` - Greater than (`>`)
- `__ge__(self, other)` - Greater than or equal (`>=`)
- `__ne__(self, other)` - Not equal (`!=`)

### 3. Arithmetic Methods

**`__add__(self, other)`** - Addition (`+`)
```python
class CartItem:
    def __init__(self, quantity):
        self.quantity = quantity

    def __add__(self, other):
        return CartItem(self.quantity + other.quantity)

    def __str__(self):
        return f"Quantity: {self.quantity}"

item1 = CartItem(5)
item2 = CartItem(3)
total = item1 + item2
print(total)  # Quantity: 8
```

**Other arithmetic methods:**
- `__sub__(self, other)` - Subtraction (`-`)
- `__mul__(self, other)` - Multiplication (`*`)
- `__truediv__(self, other)` - Division (`/`)

### 4. Container Methods

**`__len__(self)`** - Length (`len()`)
```python
class Playlist:
    def __init__(self):
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)

    def __len__(self):
        return len(self.songs)

playlist = Playlist()
playlist.add_song("Song 1")
playlist.add_song("Song 2")
print(len(playlist))  # 2
```

**`__getitem__(self, index)`** - Indexing (`obj[i]`)
```python
class Playlist:
    def __init__(self):
        self.songs = []

    def __getitem__(self, index):
        return self.songs[index]

playlist = Playlist()
playlist.songs = ["Song 1", "Song 2"]
print(playlist[0])  # Song 1

# Enables iteration!
for song in playlist:
    print(song)
```

## Complete Example

```python
class Car:
    def __init__(self, make, model, price):
        self.make = make
        self.model = model
        self.price = price

    def __str__(self):
        return f"{self.make} {self.model} - ${self.price:,}"

    def __repr__(self):
        return f"Car('{self.make}', '{self.model}', {self.price})"

    def __eq__(self, other):
        return self.make == other.make and self.model == other.model

    def __lt__(self, other):
        return self.price < other.price

# Usage
car1 = Car("Toyota", "Camry", 25000)
car2 = Car("Honda", "Civic", 22000)

print(car1)              # Toyota Camry - $25,000
print(repr(car2))        # Car('Honda', 'Civic', 22000)
print(car1 == car2)      # False
print(car2 < car1)       # True

# Sorting by price
cars = [car1, car2]
sorted_cars = sorted(cars)
print([str(c) for c in sorted_cars])
# ['Honda Civic - $22,000', 'Toyota Camry - $25,000']
```

## Quick Reference

| Operation | Magic Method | Example |
|-----------|-------------|---------|
| `print(obj)` | `__str__` | User display |
| `repr(obj)` | `__repr__` | Debug display |
| `obj1 == obj2` | `__eq__` | Equality |
| `obj1 < obj2` | `__lt__` | Less than |
| `obj1 + obj2` | `__add__` | Addition |
| `len(obj)` | `__len__` | Length |
| `obj[i]` | `__getitem__` | Indexing |

## Common Pitfall

❌ **Don't forget to return a value:**
```python
class Wrong:
    def __add__(self, other):
        self.value += other.value  # Missing return!
```

✅ **Always return:**
```python
class Correct:
    def __add__(self, other):
        return Correct(self.value + other.value)
```

## Summary

- Magic methods let your objects work with Python's built-in syntax
- They're called **automatically** by Python
- `__str__` for display, `__repr__` for debugging
- `__eq__` and `__lt__` enable comparisons and sorting
- `__add__`, `__sub__` enable arithmetic
- Make your custom objects behave like built-in types!
