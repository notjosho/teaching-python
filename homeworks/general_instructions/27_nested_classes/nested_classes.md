# Nested Classes

## What Are They?

A nested class is a class defined inside another class. The inner class exists within the namespace of the outer class.

```python
class Outer:
    class Inner:
        def __init__(self):
            self.value = "I'm inside!"
```

## Understanding Namespaces

A namespace is a container that holds names (variables, functions, classes). Nested classes create their own namespace:

```python
# Without nesting - namespace pollution
class CompanyEmployee:
    pass

class SchoolEmployee:
    pass

# With nesting - clean namespaces
class Company:
    class Employee:  # Company.Employee
        pass

class School:
    class Employee:  # School.Employee (different!)
        pass
```

**Benefits:** Same name can be used in different contexts without conflicts.

## When to Use

1. The inner class only makes sense with the outer class
2. You want to prevent namespace pollution
3. You're creating helper classes specific to the outer class

## Example 1: Company and Employee

```python
class Company:
    class Employee:
        def __init__(self, name, position):
            self.name = name
            self.position = position

        def get_info(self):
            return f"{self.name} - {self.position}"

    def __init__(self, company_name):
        self.company_name = company_name
        self.employees = []

    def hire(self, name, position):
        new_employee = self.Employee(name, position)
        self.employees.append(new_employee)

# Usage
company = Company("Tech Corp")
company.hire("Alice", "Developer")
print(company.employees[0].get_info())  # Alice - Developer
```

## Example 2: Zelda Adventure

```python
class ZeldaGame:
    class Hero:
        def __init__(self, name):
            self.name = name
            self.hearts = 3
            self.rupees = 0

        def collect_rupees(self, amount):
            self.rupees += amount
            if self.rupees >= 100:
                self.hearts += 1
                self.rupees -= 100
                return f"{self.name} gained a heart! Hearts: {self.hearts}"
            return f"{self.name}: {self.rupees} rupees"

    def __init__(self, quest_name):
        self.quest_name = quest_name
        self.heroes = []

    def start_adventure(self, hero_name):
        hero = self.Hero(hero_name)
        self.heroes.append(hero)
        return f"{hero_name} begins {self.quest_name}!"

# Usage
zelda = ZeldaGame("Quest for the Triforce")
zelda.start_adventure("Link")
zelda.heroes[0].collect_rupees(50)   # Link: 50 rupees
zelda.heroes[0].collect_rupees(60)   # Link gained a heart! Hearts: 4
```
## Accessing Nested Classes

**From inside outer class:**
```python
def create_inner(self):
    return self.Inner()  # Use self.Inner
```

**From outside:**
```python
inner = Outer.Inner()  # Through class name
```
## Summary

- Nested classes = classes inside classes
- Creates clean namespaces and prevents naming conflicts
- Access with `OuterClass.InnerClass` or `self.InnerClass`
- Use when inner class only makes sense with outer class
