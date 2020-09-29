import random


class Spell:
    def __init__(self, name, cost, dmg, type_spell):
        self.name = name
        self.cost = cost
        self.dmg = dmg
        self.type_spell = type_spell

    def generate_spell_damage(self):
        low = self.dmg - 15
        high = self.dmg + 15
        return random.randrange(low, high)

    def generate_heal(self):
        low = self.dmg - 15
        high = self.dmg + 15
        return random.randrange(low, high)

