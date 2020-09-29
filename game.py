import random

from magic import Spell
from inventory import Item


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Person:
    def __init__(self, name, hp, mp, atk, df, magic, items):
        self.maxhp = hp
        self.hp = hp
        self.maxmp = mp
        self.mp = mp
        self.atkh = atk + 10
        self.atkl = atk - 10
        self.df = df
        self.magic = magic
        self.items = items
        self.actions = ['Attack', 'Magic', "Items"]
        self.name = name

    def generate_damage(self):
        return random.randrange(self.atkl, self.atkh)

    def take_damage(self, dmg):
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0
        return self.hp

    def take_heal(self, heal):
        self.hp += heal
        if self.hp > self.maxhp:
            self.hp = self.maxhp
        return self.hp

    def take_mp(self, mp):
        self.mp += mp
        if self.mp >= self.maxmp:
            self.mp = self.max.mp
        return self.mp

    def choose_action(self):
        i = 1
        print("ACTIONS:-")
        print(self.name)
        for x in self.actions:
            print(str(i) + ':', x)
            i += 1

    def choose_magic(self):
        i = 1
        print("MAGIC:-")
        for x in self.magic:
            print(str(i) + ":", x.name, '(cost:', str(x.cost) + ')')
            i += 1

    def choose_item(self):
        i = 1
        print("ITEMS:-")
        for x in self.items:
            print(i, x['name'].name, ":", x['name'].description, "Quantity", "*", x['quantity'])
            i += 1

    def get_hp(self):
        return self.hp

    def get_max_hp(self):
        return self.maxhp

    def get_mp(self):
        return self.mp

    def get_max_mp(self):
        return self.maxmp

    def reduce_mp(self, cost):
        self.mp -= cost

    def choose_target(self, enemies):
        i = 1
        print("Choose Enemy--")

        for enemy in enemies:
            if enemy.get_hp() != 0:
                print(i, enemy.name)
                i += 1
        choice = int(input("Enter your choice:--")) - 1
        return choice

    def players_get_stats(self):

        hp_bar = ""
        hp_bar_ticks = self.hp / self.maxhp * 100 / 4

        while hp_bar_ticks > 0:
            hp_bar += "█"
            hp_bar_ticks -= 1

        while len(hp_bar) < 25:
            hp_bar += " "

        hp = str(self.hp) + "/" + str(self.maxhp)

        current_hp = ""
        if len(hp) < 9:
            decrease1 = 9 - len(hp)

            while decrease1 > 0:
                current_hp += " "
                decrease1 -= 1
            current_hp += hp
        else:
            current_hp = hp

        mp_bar = ""
        mp_bar_ticks = self.mp / self.maxmp * 100 / 10

        while mp_bar_ticks > 0:
            mp_bar += "█"
            mp_bar_ticks -= 1

        while len(mp_bar) < 10:
            mp_bar += " "

        mp = str(self.mp) + "/" + str(self.maxmp)

        current_mp = ""
        if len(mp) < 7:
            decrease2 = 7 - len(mp)

            while decrease2 > 0:
                current_mp += " "
                decrease2 -= 1
            current_mp += mp
        else:
            current_mp = mp

        print("                           _________________________               __________  ")
        print(bcolors.BOLD, self.name, bcolors.ENDC,
              current_hp, bcolors.OKGREEN, "   ", "|", hp_bar, "|", bcolors.ENDC,
              current_mp, bcolors.OKBLUE, "|", mp_bar, "|", bcolors.ENDC)

    def enemy_get_stats(self):
        en_hp_bar = ""
        en_bar_ticks = self.hp / self.maxhp * 100 / 2

        while en_bar_ticks > 0:
            en_hp_bar += "█"
            en_bar_ticks -= 1

        while len(en_hp_bar) < 50:
            en_hp_bar += " "

        hp = str(self.hp) + "/" + str(self.maxhp)

        current_hp = ""
        if len(hp) < 11:
            descrese = 11 - len(hp)

            while descrese > 0:
                current_hp += " "
                descrese -= 1
            current_hp += hp

        else:
            current_hp = hp

        print("                           __________________________________________________  ")
        print(bcolors.BOLD, self.name, bcolors.ENDC,
              current_hp, bcolors.FAIL, "  ", "|", en_hp_bar, "|", bcolors.ENDC)


"""     print("                       _________________________                __________  ")
        print(bcolors.BOLD, self.name, bcolors.ENDC,
              self.hp, "/", self.maxhp, bcolors.OKGREEN, " |█████████████████████████| ", bcolors.ENDC,
              self.mp, "/", self.maxmp, bcolors.OKBLUE, " |██████████| ", bcolors.ENDC)
"""
"""    def generate_spell_damage(self, i):
        mgl = self.magic[i]['dmg'] - 5
        mgh = self.magic[i]['dmg'] + 5
        return random.randrange(mgl, mgh)"""
"""   def get_spell_name(self, i):
        return self.magic[i]["name"]

    def get_spell_cost(self, i):
        return self.magic[i]["cost"]"""
