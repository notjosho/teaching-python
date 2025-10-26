class Person:
  def __init__(self, name):
    self._name = name

  def introduce(self):
    print (f"Hello, my name is: {self._name}")

  def walk(self):
    print (f"{self._name} is walking")

class Student(Person):
  def study(self):
    print (f"{self._name} is studying")

person = Person("John")
person.introduce()  # Expected Output: Hello, my name is John
person.walk()       # Expected Output: John is walking

student = Student("Maria")
student.introduce()  # Expected Output: Hello, my name is Maria
student.walk()       # Expected Output: Maria is walking
student.study()      # Expected Output: Maria is studying
