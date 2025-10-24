class Person:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        return print(f"Hello, my name is {self.name}")

    def walk(self):
        return print(f"{self.name} is walking")


class Student(Person):
    def study(self):
        return print(f"{self.name} is studying")


person = Person("John")
person.introduce()  # Expected Output: Hello, my name is John
person.walk()  # Expected Output: John is walking

student = Student("Maria")
student.introduce()  # Expected Output: Hello, my name is Maria
student.walk()  # Expected Output: Maria is walking
student.study()  # Expected Output: Maria is studying
