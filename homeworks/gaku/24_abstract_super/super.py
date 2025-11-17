from typing import override


class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.energy = 100

    def speak(self):
        return "Some generic sound"

    def info(self):
        return f"{self.name} is {self.age} years old"

    def eat(self, add=0):
        self.energy += 20 + add
        if self.energy > 100:
            self.energy = 100
        return self.energy

    def play(self, add=0):
        self.energy -= 15 + add
        if self.energy < 0:
            self.energy = 0
        return self.energy


class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed

    @override
    def speak(self):
        return f"{super().speak()} - but actually: Woof! Woof!"

    @override
    def info(self):
        return f"{super().info()} and is a {self.breed}"


class Cat(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    @override
    def speak(self):
        return "Meow!"

    @override
    def info(self):
        return f"{super().info()} and has {self.color} fur"


class Bird(Animal):
    def __init__(self, name, age, species):
        super().__init__(name, age)
        self.species = species
        self._flight_distance = 0

    @override
    def speak(self):
        return "Chirp chirp!"

    @override
    def info(self):
        return f"{super().info()}, is a {self.species}, and has flown {self._flight_distance} km"

    @override
    def eat(self):
        return super().eat(10)

    @override
    def play(self):
        self._flight_distance += 5
        return super().play(5)
