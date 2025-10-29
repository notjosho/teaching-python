# Test file for Homework Assignment 1
# Run with: python3 test_hw_animals.py

from hw_animals import Animal, Dog, Cat, Bird

def test_animal_creation():
    """Test that animals can be created with correct attributes"""
    dog = Dog("Buddy", 5)
    assert dog._name == "Buddy"
    assert dog._age == 5
    print("✓ Animal creation test passed")

def test_base_animal_class():
    """Test that base Animal class works correctly"""
    animal = Animal("Generic", 3)
    assert animal._name == "Generic"
    assert animal._age == 3
    assert animal.make_sound() == "Generic animal sound"
    assert animal.eat("food") == "Animal eats food"
    assert animal.get_description() == "Generic is 3 years old"
    print("✓ Base Animal class test passed")

def test_polymorphism_make_sound():
    """Test that different animals make different sounds"""
    dog = Dog("Max", 3)
    cat = Cat("Whiskers", 2)
    bird = Bird("Tweety", 1)

    assert dog.make_sound() == "Woof!"
    assert cat.make_sound() == "Meow!"
    assert bird.make_sound() == "Tweet!"
    print("✓ Polymorphism sound test passed")

def test_eat_method():
    """Test that animals have different eating behaviors"""
    dog = Dog("Rex", 4)
    cat = Cat("Felix", 3)

    assert dog.eat("bone") == "Dog eats bone"
    assert cat.eat("fish") == "Cat eats fish"
    print("✓ Eat method test passed")

def test_unique_methods():
    """Test that derived classes have unique methods"""
    dog = Dog("Charlie", 2)
    bird = Bird("Rio", 1)

    assert dog.fetch() == "Dog fetches the ball"
    assert bird.fly() == "Bird is flying"
    print("✓ Unique methods test passed")

def test_get_description():
    """Test that get_description provides information about the animal"""
    cat = Cat("Luna", 4)

    assert cat.get_description() == "Luna is 4 years old"
    print("✓ Get description test passed")

if __name__ == "__main__":
    print("Running Animal Kingdom Tests...\n")

    try:
        test_animal_creation()
        test_base_animal_class()
        test_polymorphism_make_sound()
        test_eat_method()
        test_unique_methods()
        test_get_description()

        print("\n" + "="*50)
        print("ALL TESTS PASSED! Great job! 🎉")
        print("="*50)
    except AssertionError as e:
        print(f"\n❌ Test failed: {e}")
    except Exception as e:
        print(f"\n❌ Error running tests: {e}")
