from super import Animal, Dog, Cat, Bird

def test_animal_class():
    """Test Animal parent class"""
    print("Testing Animal class...")
    animal = Animal("Generic", 5)

    # Test attributes
    assert animal.name == "Generic", f"Expected name 'Generic', got {animal.name}"
    assert animal.age == 5, f"Expected age 5, got {animal.age}"
    assert animal.energy == 100, f"Expected energy 100, got {animal.energy}"
    print(f"  ✓ Animal attributes: name={animal.name}, age={animal.age}, energy={animal.energy}")

    # Test speak method
    sound = animal.speak()
    assert sound == "Some generic sound", f"Unexpected sound: {sound}"
    print(f"  ✓ Animal speak: {sound}")

    # Test info method
    info = animal.info()
    assert "Generic" in info and "5" in info, f"Info missing expected data: {info}"
    print(f"  ✓ Animal info: {info}")

    # Test eat method
    energy = animal.eat()
    assert energy == 100, f"Expected energy 100 (already at max), got {energy}"
    print(f"  ✓ Animal eat: energy={energy}")

    # Test play method
    energy = animal.play()
    assert energy == 85, f"Expected energy 85 (100-15), got {energy}"
    print(f"  ✓ Animal play: energy={energy}")

    print("Animal class tests passed!\n")

def test_dog_class():
    """Test Dog class and super() usage"""
    print("Testing Dog class...")
    dog = Dog("Buddy", 3, "Golden Retriever")

    # Test inherited attributes
    assert dog.name == "Buddy", f"Expected name 'Buddy', got {dog.name}"
    assert dog.age == 3, f"Expected age 3, got {dog.age}"
    print(f"  ✓ Dog inherited attributes: name={dog.name}, age={dog.age}")

    # Test additional attribute
    assert dog.breed == "Golden Retriever", f"Expected breed 'Golden Retriever', got {dog.breed}"
    print(f"  ✓ Dog breed: {dog.breed}")

    # Test speak method (uses super())
    sound = dog.speak()
    assert "Some generic sound" in sound, f"Dog speak should include parent's sound: {sound}"
    assert "Woof" in sound, f"Dog speak should include 'Woof': {sound}"
    print(f"  ✓ Dog speak: {sound}")

    # Test info method (uses super())
    info = dog.info()
    assert "Buddy" in info and "3" in info and "Golden Retriever" in info, f"Info missing expected data: {info}"
    print(f"  ✓ Dog info: {info}")

    print("Dog class tests passed!\n")

def test_cat_class():
    """Test Cat class and super() usage"""
    print("Testing Cat class...")
    cat = Cat("Whiskers", 2, "orange")

    # Test inherited attributes
    assert cat.name == "Whiskers", f"Expected name 'Whiskers', got {cat.name}"
    assert cat.age == 2, f"Expected age 2, got {cat.age}"
    print(f"  ✓ Cat inherited attributes: name={cat.name}, age={cat.age}")

    # Test additional attribute
    assert cat.color == "orange", f"Expected color 'orange', got {cat.color}"
    print(f"  ✓ Cat color: {cat.color}")

    # Test speak method
    sound = cat.speak()
    assert sound == "Meow!", f"Expected 'Meow!', got {sound}"
    print(f"  ✓ Cat speak: {sound}")

    # Test info method (uses super())
    info = cat.info()
    assert "Whiskers" in info and "2" in info and "orange" in info, f"Info missing expected data: {info}"
    print(f"  ✓ Cat info: {info}")

    print("Cat class tests passed!\n")

def test_bird_class():
    """Test Bird class with stateful methods using super()"""
    print("Testing Bird class...")
    bird = Bird("Tweety", 1, "Canary")

    # Test inherited attributes
    assert bird.name == "Tweety", f"Expected name 'Tweety', got {bird.name}"
    assert bird.age == 1, f"Expected age 1, got {bird.age}"
    assert bird.energy == 100, f"Expected energy 100, got {bird.energy}"
    print(f"  ✓ Bird inherited attributes: name={bird.name}, age={bird.age}, energy={bird.energy}")

    # Test additional attributes
    assert bird.species == "Canary", f"Expected species 'Canary', got {bird.species}"
    assert bird.flight_distance == 0, f"Expected flight_distance 0, got {bird.flight_distance}"
    print(f"  ✓ Bird attributes: species={bird.species}, flight_distance={bird.flight_distance}")

    # Test speak method
    sound = bird.speak()
    assert sound == "Chirp chirp!", f"Expected 'Chirp chirp!', got {sound}"
    print(f"  ✓ Bird speak: {sound}")

    # Test info method
    info = bird.info()
    assert "Tweety" in info and "1" in info and "Canary" in info and "0" in info, f"Info missing expected data: {info}"
    print(f"  ✓ Bird info: {info}")

    # Test play method with super() - decreases energy by 15+5=20, adds 5 to flight_distance
    energy = bird.play()
    assert energy == 80, f"Expected energy 80 (100-20), got {energy}"
    assert bird.flight_distance == 5, f"Expected flight_distance 5, got {bird.flight_distance}"
    print(f"  ✓ Bird play: energy={energy}, flight_distance={bird.flight_distance}")

    # Test eat method with super() - increases energy by 20+10=30
    energy = bird.eat()
    assert energy == 100, f"Expected energy 100 (80+30, capped at 100), got {energy}"
    print(f"  ✓ Bird eat: energy={energy}")

    # Test multiple plays
    bird.play()
    bird.play()
    assert bird.energy == 60, f"Expected energy 60 (100-40), got {bird.energy}"
    assert bird.flight_distance == 15, f"Expected flight_distance 15, got {bird.flight_distance}"
    print(f"  ✓ Bird multiple plays: energy={bird.energy}, flight_distance={bird.flight_distance}")

    print("Bird class tests passed!\n")

def test_inheritance():
    """Test that Dog, Cat, and Bird properly inherit from Animal"""
    print("Testing inheritance...")

    dog = Dog("Max", 4, "Labrador")
    cat = Cat("Mittens", 1, "black")
    bird = Bird("Polly", 2, "Parrot")

    assert isinstance(dog, Animal), "Dog should be instance of Animal"
    print("  ✓ Dog inherits from Animal")

    assert isinstance(cat, Animal), "Cat should be instance of Animal"
    print("  ✓ Cat inherits from Animal")

    assert isinstance(bird, Animal), "Bird should be instance of Animal"
    print("  ✓ Bird inherits from Animal")

    # Test that child classes can access parent methods
    assert hasattr(dog, 'speak'), "Dog should have speak method"
    assert hasattr(dog, 'info'), "Dog should have info method"
    assert hasattr(cat, 'speak'), "Cat should have speak method"
    assert hasattr(cat, 'info'), "Cat should have info method"
    assert hasattr(bird, 'speak'), "Bird should have speak method"
    assert hasattr(bird, 'info'), "Bird should have info method"
    assert hasattr(bird, 'eat'), "Bird should have eat method"
    assert hasattr(bird, 'play'), "Bird should have play method"
    print("  ✓ Child classes have access to parent methods")

    print("Inheritance tests passed!\n")

if __name__ == "__main__":
    print("=" * 50)
    print("Running tests for super.py")
    print("=" * 50 + "\n")

    test_animal_class()
    test_dog_class()
    test_cat_class()
    test_bird_class()
    test_inheritance()

    print("=" * 50)
    print("All tests passed successfully!")
    print("=" * 50)
