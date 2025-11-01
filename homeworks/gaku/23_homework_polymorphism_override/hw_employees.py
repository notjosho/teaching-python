from typing import override


class Employee:
    def __init__(self, name, salary):
        self._name = name
        self._salary = salary

    def get_bonus(self):
        bonus = 0.10 * self._salary
        return int(bonus)

    def work(self):
        return "Working on tasks"

    def get_info(self):
        return f"{self._name} earns {self._salary}"


class Manager(Employee):
    @override
    def get_bonus(self):
        bonus = 0.20 * self._salary
        return bonus

    def work(self):
        return "Managing the team and planning projects"


class Developer(Employee):
    @override
    def get_bonus(self):
        bonus = 0.15 * self._salary
        return bonus

    @override
    def work(self):
        return "Writing code and fixing bugs"

    def code(self):
        return "Writing Python code"


class Intern(Employee):
    @override
    def get_bonus(self):
        bonus = 0.05 * self._salary
        return bonus

    @override
    def work(self):
        return "Learning and helping with tasks"

    def learn(self):
        return "Learning new skills"
