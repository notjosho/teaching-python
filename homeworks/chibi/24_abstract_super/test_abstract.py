from abstract import Shape, Rectangle, Circle

def test_rectangle():
    """Test Rectangle class implementation"""
    print("Testing Rectangle...")
    rect = Rectangle(5, 3)

    # Test area calculation
    area = rect.area()
    assert area == 15, f"Expected area 15, got {area}"
    print(f"  ✓ Rectangle area: {area}")

    # Test perimeter calculation
    perimeter = rect.perimeter()
    assert perimeter == 16, f"Expected perimeter 16, got {perimeter}"
    print(f"  ✓ Rectangle perimeter: {perimeter}")

    print("Rectangle tests passed!\n")

def test_circle():
    """Test Circle class implementation"""
    print("Testing Circle...")
    circle = Circle(4)

    # Test area calculation (pi * r^2)
    area = circle.area()
    expected_area = 3.14 * 16
    assert area == expected_area, f"Expected area {expected_area}, got {area}"
    print(f"  ✓ Circle area: {area}")

    # Test perimeter calculation (2 * pi * r)
    perimeter = circle.perimeter()
    expected_perimeter = 2 * 3.14 * 4
    assert perimeter == expected_perimeter, f"Expected perimeter {expected_perimeter}, got {perimeter}"
    print(f"  ✓ Circle perimeter: {perimeter}")

    print("Circle tests passed!\n")

def test_abstract_class():
    """Test that Shape cannot be instantiated directly"""
    print("Testing abstract class constraint...")

    try:
        shape = Shape()
        print("  ✗ ERROR: Shape should not be instantiable!")
        assert False, "Shape class should not allow instantiation"
    except TypeError as e:
        print(f"  ✓ Correctly prevented Shape instantiation: {e}")

    print("Abstract class tests passed!\n")

def test_inheritance():
    """Test that Rectangle and Circle inherit from Shape"""
    print("Testing inheritance...")

    rect = Rectangle(10, 5)
    circle = Circle(3)

    assert isinstance(rect, Shape), "Rectangle should be instance of Shape"
    print("  ✓ Rectangle inherits from Shape")

    assert isinstance(circle, Shape), "Circle should be instance of Shape"
    print("  ✓ Circle inherits from Shape")

    print("Inheritance tests passed!\n")

if __name__ == "__main__":
    print("=" * 50)
    print("Running tests for abstract.py")
    print("=" * 50 + "\n")

    test_rectangle()
    test_circle()
    test_abstract_class()
    test_inheritance()

    print("=" * 50)
    print("All tests passed successfully!")
    print("=" * 50)
