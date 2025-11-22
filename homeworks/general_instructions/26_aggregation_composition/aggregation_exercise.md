# Exercise: Restaurant Menu System (Aggregation)

## Concept: Aggregation (The "Has-A" Relationship)

Aggregation is a type of relationship between classes where one class **contains references** to objects of another class, but those objects can exist independently.
Think of it this way:

- A **Restaurant** has menu items, but menu items can exist without the restaurant
- If the restaurant closes, the concept of a "burger" or "salad" still makes sense on its own
- The contained objects are **not owned** by the container - they are **referenced**
  **Simple example of aggregation:**

```python
# The MenuItem exists independently
burger = MenuItem("Burger", 8.99, "Main Course")
# The Restaurant references the MenuItem (doesn't create it)
restaurant = Restaurant("Joe's Diner")
restaurant.add_item(burger)  # Adding a reference to an existing object
```

## `:.2f` Format Specifier

A **format specifier** is a set of instructions that tells Python how to transform and display a value. It controls decimal places, alignment, data type, and more. Without format specifiers, numbers display inconsistently. With them, you get professional, controlled output.
The basic syntax is:

```
f"{value:FORMATSPEC}"
     ↑
     Format specifier starts with a colon
```

### Breaking down `:.2f`

| Component | What it does                                            | Example                                        |
| --------- | ------------------------------------------------------- | ---------------------------------------------- |
| `:`       | Signals the start of format instructions                | Separates value from formatting                |
| `.2`      | Precision - show exactly 2 decimal places               | `8.5` becomes `8.50`, `12.999` becomes `13.00` |
| `f`       | Format type - `f` means floating-point (decimal) number | Works with numbers like `3.14`, `7.0`, `99.5`  |

### More format specifier examples

```python
# Different decimal places
value = 3.14159
print(f"{value:.1f}")        # 3.1 (1 decimal place)
print(f"{value:.3f}")        # 3.142 (3 decimal places)
# Percentage formatting
percentage = 0.856
print(f"{percentage:.1%}")   # 85.6%
```

## Aggregation Exercise

Implement the complete Restaurant Menu System with the following requirements:

1. Create the `MenuItem` class with `name`, `price`, and `category` attributes
2. Create the `Restaurant` class with these methods:
   - `__init__(self, name)`: Initialize the restaurant with a name and an empty list for menu items
   - `add_item(self, menu_item)`: Add a MenuItem object to the menu_items list
   - `display_menu(self)`: Display all menu items grouped by category
     - Build a formatted menu string with:
       - Header: `===== RestaurantName Menu =====` followed by a blank line
       - Group items by their category:
         - Create a dictionary to organize items by category
         - Loop through menu_items and add each item to its category in the dictionary
       - For each category, include `Category: CategoryName` then list each item as `- ItemName: $Price` (use `:.2f` for price formatting)
     - Print the formatted menu string
     - Return the formatted menu string
   - `find_items_in_price_range(self, min_price, max_price)`: Find items within a price range
     - Filter items where price is between min_price and max_price (inclusive)
     - Return the list of filtered items
   - `delete_item(self, item_name)`: Remove a menu item by name
     - Remove the item from the menu_items list
     - This demonstrates aggregation: deleting from one restaurant doesn't affect other restaurants or the item itself

## Grouping Items by Category - Hint

To group items by category, use a dictionary approach:

- Create an empty dictionary before looping through items
- For each item, check if its category key exists in the dictionary
- If it doesn't exist, create a new empty list for that category
- Add each item to its category's list
- Then loop through the dictionary to display each category and its items

## Why Is This Aggregation?

This example demonstrates aggregation because:

1. **Independent Existence**: MenuItem objects are created **before** being added to the Restaurant. They exist independently.
2. **Shared References**: The same MenuItem could potentially be added to multiple restaurants (imagine a franchise sharing menu items).
3. **No Ownership**: The Restaurant does not create or destroy MenuItem objects - it simply holds references to them.
4. **Loose Coupling**: If we delete the Restaurant object, the MenuItem objects would still exist in memory (if referenced elsewhere).
   Compare this to **composition** where:

- The container creates and owns the contained objects
- Contained objects cannot exist without the container
- Deleting the container destroys the contained objects
