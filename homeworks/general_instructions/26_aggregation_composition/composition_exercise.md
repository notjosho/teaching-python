# Exercise: Smartphone System (Composition)

## Concept: Composition (Owns-A Relationship)

Composition represents a relationship where one object directly **owns** its components. The components are created inside the constructor and cannot exist independently from their container object. This is called an "owns-a" relationship.
The key difference: The container class receives simple values as parameters and creates its own component objects internally in the constructor. The components belong exclusively to that container.

## Helpful Syntax Concepts

### Integer Division with `//`

The `//` operator divides and rounds down to the nearest whole number:

```python
minutes = 45
charge_reduction = minutes // 10  # Result: 4 (not 4.5)

minutes = 23
charge_reduction = minutes // 10  # Result: 2 (not 2.3)
```

This is useful when you need whole number results, like "reduce 1% for every 10 minutes".

### Using `max()` to Prevent Negative Values

The `max()` function returns the larger of two values:

```python
charge = 5
reduction = 10
new_charge = max(0, charge - reduction)  # Result: 0 (not -5)
```

This ensures values never go below zero.

## Composition Exercise

Create a Smartphone system where a smartphone owns a Battery and Processor. These components are created inside the Smartphone's constructor.

## Implementation Steps

1. Create a `Battery` class with:
   - `capacity` attribute (in mAh, received as parameter)
   - `charge_level` attribute initialized to 100 (percentage)
2. Create a `Processor` class with:
   - `model` attribute (received as parameter)
   - `speed` attribute (in GHz, received as parameter)
3. Create a `Smartphone` class with:
   - Parameters: `brand`, `model`, `battery_capacity`, `processor_model`, `processor_speed`
   - Store `brand` and `model` as attributes
   - Create a `Battery` instance inside the constructor using `battery_capacity`
   - Create a `Processor` instance inside the constructor using `processor_model` and `processor_speed`
4. Add a `get_specs()` method to `Smartphone` that returns a string in this format:
   ```
   Apple iPhone 14 - Processor: A15 Bionic (3.2GHz) - Battery: 3279mAh (100% charged)
   ```
5. Add a `use_phone(minutes)` method to `Smartphone` that:
   - Calculates charge reduction: 1% for every 10 minutes (use `//`)
   - Updates `self.battery.charge_level` (cannot go below 0)
   - Returns the new charge level
6. Add a `get_battery_status()` method to `Smartphone` that:
   - Returns "High" if charge_level is above 50%
   - Returns "Normal" if charge_level is between 20% and 50%
   - Returns "Low" if charge_level is 20% or below

## Why This Is Composition

This example demonstrates composition because:

1. **Components are created inside `__init__`**: The `Battery` and `Processor` objects are instantiated within the `Smartphone` constructor, not passed in from outside.
2. **Strong ownership**: Each smartphone has its own unique battery and processor. These components belong exclusively to that phone.
3. **Lifecycle dependency**: If a `Smartphone` object is deleted, its `Battery` and `Processor` are also deleted - they have no independent existence.
4. **Parent controls creation**: The `Smartphone` decides how to create its components based on the values it receives.
   **Contrast with Aggregation:**

```python
# AGGREGATION (different pattern - objects created outside):
battery = Battery(3279)
processor = Processor("A15", 3.2)
phone = Smartphone("Apple", "iPhone", battery, processor)  # Receives existing objects
# COMPOSITION (our pattern - objects created inside):
phone = Smartphone("Apple", "iPhone", 3279, "A15", 3.2)  # Creates objects internally
```

In composition, the parent class receives simple values and builds its own components. In aggregation, the parent receives already-existing objects that could be shared or exist independently.
