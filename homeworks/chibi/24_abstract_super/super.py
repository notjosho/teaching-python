class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.energy = 100

    def speak(self):
        return "Some generic sound"

    def info(self):
        return f"{self.name} is {self.age} years old"

    def eat(self):
        self.energy += 20
        if self.energy > 100:
            self.energy = 100
        return self.energy

    def play(self):
        self.energy -= 15
        if self.energy < 0:
            self.energy = 0
        return self.energy


class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed

    def speak(self):
        parent_sound = super().speak()
        return f"{parent_sound} - but actually: Woof! Woof!"

    def info(self):
        parent_info = super().info()
        return f"{parent_info} and is a {self.breed}"


class Cat(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def speak(self):
        return "Meow!"

    def info(self):
        parent_info = super().info()
        return f"{parent_info} and has {self.color} fur"


class Bird(Animal):
    def __init__(self, name, age, species):
        super().__init__(name, age)
        self.species = species
        self.flight_distance = 0

    def speak(self):
        return "Chirp chirp!"

    def info(self):
        parent_info = super().info()
        return f"{parent_info}, is a {self.species}, and has flown {self.flight_distance} km"

    def eat(self):
        energy = super().eat()
        self.energy += 10
        if self.energy > 100:
            self.energy = 100
        return self.energy

    def play(self):
        energy = super().play()
        self.flight_distance += 5
        self.energy -= 5
        if self.energy < 0:
            self.energy = 0
        return self.energy


if __name__ == "__main__":
    dog = Dog("Buddy", 3, "Golden Retriever")
    cat = Cat("Whiskers", 2, "black")
    bird = Bird("Tweety", 1, "canary")

    print(dog.speak())
    print(dog.info())
    print(dog.play(), dog.eat())

    print(cat.speak())
    print(cat.info())

    print(bird.speak())
    print(bird.info())
    print("After play:", bird.play())
    print("After eat:", bird.eat())
    print(bird.info())