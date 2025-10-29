# Test file for Homework Assignment 2
# Run with: python3 test_hw_employees.py

from hw_employees import Employee, Manager, Developer, Intern

def test_employee_creation():
    """Test that employees can be created with correct attributes"""
    dev = Developer("Alice", 80000)
    assert dev._name == "Alice"
    assert dev._salary == 80000
    print("✓ Employee creation test passed")

def test_base_employee_class():
    """Test that base Employee class works correctly"""
    employee = Employee("John", 50000)
    assert employee._name == "John"
    assert employee._salary == 50000
    assert employee.get_bonus() == 5000  # 10% of 50000
    assert employee.work() == "Working on tasks"
    assert employee.get_info() == "John earns 50000"
    print("✓ Base Employee class test passed")

def test_bonus_calculation():
    """Test that different employees get different bonuses"""
    manager = Manager("Bob", 100000)
    developer = Developer("Carol", 80000)
    intern = Intern("Dave", 40000)

    # Manager gets 20% bonus
    assert manager.get_bonus() == 20000, f"Expected 20000, got {manager.get_bonus()}"

    # Developer gets 15% bonus
    assert developer.get_bonus() == 12000, f"Expected 12000, got {developer.get_bonus()}"

    # Intern gets 5% bonus
    assert intern.get_bonus() == 2000, f"Expected 2000, got {intern.get_bonus()}"

    print("✓ Bonus calculation test passed")

def test_work_method():
    """Test that different employees describe their work differently"""
    manager = Manager("Emma", 100000)
    developer = Developer("Frank", 80000)
    intern = Intern("Grace", 40000)

    assert manager.work() == "Managing the team and planning projects"
    assert developer.work() == "Writing code and fixing bugs"
    assert intern.work() == "Learning and helping with tasks"

    print("✓ Work method test passed")

def test_unique_methods():
    """Test that derived classes have unique methods"""
    developer = Developer("Helen", 80000)
    intern = Intern("Ivan", 40000)

    assert developer.code() == "Writing Python code"
    assert intern.learn() == "Learning new skills"

    print("✓ Unique methods test passed")

def test_get_info():
    """Test that get_info provides employee information"""
    manager = Manager("Jack", 100000)

    assert manager.get_info() == "Jack earns 100000"
    print("✓ Get info test passed")

def test_polymorphism():
    """Test that all employees can be treated as Employee objects"""
    employees = [
        Manager("Kate", 100000),
        Developer("Leo", 80000),
        Intern("Mia", 40000)
    ]

    # All employees should have the required methods and return correct types
    for employee in employees:
        bonus = employee.get_bonus()
        assert isinstance(bonus, (int, float)), "Bonus should be a number"
        assert bonus > 0, "Bonus should be positive"

        work_desc = employee.work()
        assert isinstance(work_desc, str), "Work description should be a string"

    print("✓ Polymorphism test passed")

if __name__ == "__main__":
    print("Running Employee Management System Tests...\n")

    try:
        test_employee_creation()
        test_base_employee_class()
        test_bonus_calculation()
        test_work_method()
        test_unique_methods()
        test_get_info()
        test_polymorphism()

        print("\n" + "="*50)
        print("ALL TESTS PASSED! Excellent work! 🎉")
        print("="*50)
    except AssertionError as e:
        print(f"\n❌ Test failed: {e}")
    except Exception as e:
        print(f"\n❌ Error running tests: {e}")
