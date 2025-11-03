class Employee:
  def __init__(self, name, salary):
     self._name = name
     self._salary = salary

  def get_bonus(self):
    return self._salary * 0.10

  def work(self):
    return "Working on tasks"

  def get_info(self):
    return f"{self._name} earns {self._salary}"


class Manager(Employee):
  def get_bonus(self):
    return self._salary * 0.20

  def work(self):
    return "Managing the team and planning projects"


class Developer(Employee):
  def get_bonus(self):
    return self._salary * 0.15

  def work(self):
    return "Writing code and fixing bugs"

  def code(self):
    return "Writing Python code"


class Intern(Employee):
  def get_bonus(self):
    return self._salary * 0.05

  def work(self):
    return "Learning and helping with tasks"

  def learn(self):
    return "Learning new skills"
