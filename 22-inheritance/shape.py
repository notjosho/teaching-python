class Shape:
  def __init__ (self, name):
    self._name = name

  def describe(self):
    print(f"{self._name} is a shape")
  
  def draw(self):
    print(f"Drawing {self._name}")

class Polygon(Shape):
  
  def has_sides(self):
    print(f"{self._name} has multiple sides")

class Triangle(Polygon):
  
  def count_angles(self):
    print(f"{self._name} has 3 angles")

shape = Shape("Circle")
shape.describe()  # Expected Output: Circle is a shape
shape.draw()      # Expected Output: Drawing Circle

polygon = Polygon("Pentagon")
polygon.describe()   # Expected Output: Pentagon is a shape
polygon.has_sides()  # Expected Output: Pentagon has multiple sides
polygon.draw()       # Expected Output: Drawing Pentagon

triangle = Triangle("Right Triangle")
triangle.describe()      # Expected Output: Right Triangle is a shape
triangle.has_sides()     # Expected Output: Right Triangle has multiple sides
triangle.count_angles()  # Expected Output: Right Triangle has 3 angles
triangle.draw()          # Expected Output: Drawing Right Triangle