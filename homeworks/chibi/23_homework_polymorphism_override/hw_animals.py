from typing import override

class Animal:
  def __init__(self, name, age):
    self._name = name
    self._age = age

  def make_sound(self):
    return "Generic animal sound"

  def eat(self, food):
    return f"Animal eats {food}"

  def get_description(self):
    return f"{self._name} is {self._age} years old"


class Dog(Animal):
  @override  
  def make_sound(self):
    return "Woof!"

  def eat(self, food):
    return f"Dog eats {food}"

  def fetch(self):
    return "Dog fetches the ball"


class Cat(Animal):
  @override  
  def make_sound(self):
    return "Meow!"

  def eat(self, food):
    return f"Cat eats {food}"


class Bird(Animal):
  @override  
  def make_sound(self):
    return "Tweet!"

  def eat(self, food):
    return f"Bird eats {food}"

  def fly(self):
    return "Bird is flying"

