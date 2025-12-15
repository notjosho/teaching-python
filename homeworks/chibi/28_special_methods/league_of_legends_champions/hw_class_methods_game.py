# Progressive Champion Class Exercise
# You will build this class across 3 exercises

import random

class Champion:
    # Class variables - shared across all champions
    total_champions = 0
    total_mastery_points = 0
    valid_roles = ["Top", "Jungle", "Mid", "ADC", "Support"]

    def __init__(self, summoner_name, champion_name, role):
        # TODO: Add validation in Exercise 1 using validate_summoner_name() and is_valid_role()
        self.summoner_name = summoner_name
        self.champion_name = champion_name
        self.role = role
        self.level = 1
        self.health = 600
        self.max_health = 600
        self.mana = 300
        self.max_mana = 300
        self.mastery_points = 0
        # TODO: Use generate_summoner_id() in Exercise 1
        self.summoner_id = f"S{random.randint(1000, 9999)}"

        Champion.total_champions += 1

    # INSTANCE METHODS (already provided)
    def attack(self, target):
        # TODO: Use calculate_damage() in Exercise 1
        damage = 50 + (self.level - 1) * 3 + random.randint(0, 15)
        target.take_damage(damage)
        return f"{self.summoner_name}'s {self.champion_name} attacks {target.summoner_name}'s {target.champion_name} for {damage} damage!"

    def take_damage(self, amount):
        self.health -= amount
        if self.health < 0:
            self.health = 0
        return f"{self.summoner_name}'s {self.champion_name} takes {amount} damage! HP: {self.health}/{self.max_health}"

    def heal(self, amount):
        old_health = self.health
        self.health += amount
        if self.health > self.max_health:
            self.health = self.max_health
        actual_heal = self.health - old_health
        return f"{self.champion_name} heals for {actual_heal} HP! HP: {self.health}/{self.max_health}"

    def gain_mastery(self, points):
        self.mastery_points += points
        Champion.total_mastery_points += points

        points_needed = self.level * 100
        if self.mastery_points >= points_needed and self.level < 18:
            return self.level_up()
        return f"{self.champion_name} gains {points} mastery points! ({self.mastery_points}/{points_needed})"

    def level_up(self):
        if self.level < 18:
            self.level += 1
            self.max_health += 80
            self.health = self.max_health
            self.max_mana += 40
            self.mana = self.max_mana
            return f"{self.champion_name} leveled up to Level {self.level}! Max HP: {self.max_health}, Max Mana: {self.max_mana}!"
        return f"{self.champion_name} is already max level (18)!"

    def get_info(self):
        return f"[{self.summoner_id}] {self.summoner_name}'s {self.champion_name} ({self.role}) - Level {self.level} - HP: {self.health}/{self.max_health} - Mana: {self.mana}/{self.max_mana} - Mastery: {self.mastery_points}"

    # EXERCISE 1: STATIC METHODS - Utility functions (don't need self or cls)
    # TODO: Implement validate_summoner_name(summoner_name)
    # TODO: Implement is_valid_role(role)
    # TODO: Implement calculate_damage(base_ad, level)
    # TODO: Implement generate_summoner_id()
    # TODO: Implement find_highest_level_champion(champions)

    # EXERCISE 2: CLASS METHODS - Work with class-level data
    # TODO: Implement get_champion_count(cls)
    # TODO: Implement get_total_mastery(cls)
    # TODO: Implement get_average_level(cls, champions)
    # TODO: Implement get_highest_level(cls, champions)

    # EXERCISE 3: MAGIC METHODS - Customize Python behavior
    # TODO: Implement __str__(self)
    # TODO: Implement __repr__(self)
    # TODO: Implement __eq__(self, other)
    # TODO: Implement __lt__(self, other) for level comparison
