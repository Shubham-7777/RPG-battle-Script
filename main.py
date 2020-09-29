from game import Person, bcolors
from magic import Spell
from inventory import Item
import random

print("\n")
print(bcolors.FAIL + bcolors.BOLD + "An Enemy Attacks!!" + bcolors.ENDC)
print(bcolors.OKBLUE,bcolors.BOLD, "NAME                                   HP                            MP", bcolors.ENDC)
# print("\n\n")

"""magic = [{"name": "Fire", "cost": 10, "dmg": 100},
         {"name": "Thunder", "cost": 10, "dmg": 120},
         {"name": "Blizzard", "cost": 10, "dmg": 80}]
"""

# Instantiate Black magic
# (self, name, cost, dmg, type_spell):
fire = Spell("Fire", 30, 332, "black")
thunder = Spell("Thunder", 40, 488, "black")
blizzard = Spell("Blizzard", 10, 145, "black")
meteor = Spell("Meteor", 50, 650, "black")
quake = Spell("Quake", 20, 256, "black")

# Instantiate White Magic
cure = Spell("Cure", 80, 1000, "white")
cura = Spell("Cura", 100, 1500, "white")

# Instantiate Inventory
# (self, name, types, description, prop)
potion = Item("Potion", "potion", "Heals 50 HP", 50)
hipotion = Item("Hi-Potion", "potion", "Heals 100 HP", 100)
superpotion = Item("Super-Potion", "potion", "Heals 150 HP", 150)
elixer = Item("Elixer", "elixer", "Fully restores HP/MP", 99999)
hielixer = Item("MegaElixer", "elixer", "Fully restores HP/MP of every player", 99999)

grenade = Item("Grenade", "attack", "Deals 500 damage", 500)

player_spells = [fire, thunder, blizzard, meteor, quake, cure, cura]
# player_items = [potion, hipotion, superpotion, elixer, hielixer, grenade])
player_items = [{"name": potion, "quantity": 15},
                {"name": hipotion, "quantity": 10},
                {"name": superpotion, "quantity": 5},
                {"name": elixer, "quantity": 5},
                {"name": hielixer, "quantity": 3},
                {"name": grenade, "quantity": 2}]

enemy_spells = [fire, meteor, cure]
enemy_items = [{"name": superpotion, "quantity": 5},
               {"name": elixer, "quantity": 5},
               {"name": hielixer, "quantity": 3},
               {"name": grenade, "quantity": 2}]

# Instantiate People
# (self, name, hp, mp, atk, df, magic, items):
player1 = Person("Valos: ", 5600, 165, 235, 34, player_spells, player_items)
player2 = Person("Nick:  ", 6500, 165, 307, 34, player_spells, player_items)
player3 = Person("Robot: ", 4400, 165, 468, 34, player_spells, player_items)

enemy1 = Person("Mega: ", 10800, 165, 540, 25, enemy_spells, enemy_items)
enemy2 = Person("Hela: ", 4600, 165, 326, 25, enemy_spells, enemy_items)
enemy3 = Person("Inox: ", 3800, 165, 432, 25, enemy_spells, enemy_items)
players = [player1, player2, player3]
enemies = [enemy1, enemy2, enemy3]
# just for stats
running = True
i = 0

"""            if enemy1.hp == 0 and enemy1.hp == 0 and enemy3.hp == 0:
                print("Player Won")
                running = False
        # for player in players:
            if player1.hp == 0 and player1.hp == 0 and player1.hp == 0:
                print("Enemy Won")
                running = False
"""
"""print(enemy.name, "remaining health is", enemy.get_hp())
        print(player1.name, player1.hp)
        print(player2.name, player2.hp)
        print(player3.name, player3.hp)"""
while running:
    for player in players:
        player.players_get_stats()
    # print('\n')
    for enemy in enemies:
        enemy.enemy_get_stats()

    for player in players:
        # print("==============================")
        player.choose_action()
        choice = int(input("Choose action:-"))
        index = choice - 1
        x = player.actions
        # =========================================================================================================
        # PLAYER
        # NORMAL ATTACK
        if index == -1:
            continue

        if index == 0 or not x:
            dmg = player.generate_damage()
            enemy = player.choose_target(enemies)
            enemies[enemy].take_damage(dmg)
            # print("======================================")
            print(player.name, "attacked for", dmg, "to", enemies[enemy].name)

            if enemies[enemy].get_hp() == 0:
                del enemies[enemy]
        # "points of damage. enemy HP:", enemy.get_hp(), 'Player HP', player.get_hp())

        # =========================================================================================================
        # MAGIC

        elif index == 1:

            player.choose_magic()
            magic_choice = int(input("Choose magic:--")) - 1
            """magic_dmg = player.generate_spell_damage(magic_choice)
                enemy.take_damage(magic_dmg)
                spell = player.get_spell_name(magic_choice)
                magic_cost = player.get_spell_cost(magic_choice)"""
            current_mp = player.get_mp()

            spell = player.magic[magic_choice]
            magic_dmg = spell.generate_spell_damage()

            if magic_choice == -1:
                continue

            if spell.cost > current_mp:
                print("\nLow Mp, You cannot use the magic\n")
                continue

            if spell.type_spell == "white":
                player.reduce_mp(spell.cost)
                magic_heal = spell.generate_heal()
                a = player.take_heal(magic_heal)
                print("Player used ", spell.name, "top heal for", magic_heal, "to", enemy.name)

            elif spell.type_spell == "black":
                player.reduce_mp(spell.cost)
                spell_damage = spell.generate_spell_damage()
                enemy = player.choose_target(enemies)
                enemies[enemy].take_damage(spell_damage)
                print(player.name, "attacked with", spell.name, "damage of", spell_damage, "to", enemies[enemy].name)

                if enemies[enemy].get_hp() == 0:
                    del enemies[enemy]
        # elif magic_choice == 6 or magic_choice == 7:
        # =========================================================================================================
        # ITEMS

        elif index == 2:
            player.choose_item()
            choice_item = int(input("Choose Item:- ")) - 1
            item = player.items[choice_item]['name']

            if choice_item == -1:
                continue

            if player.items[choice_item]['quantity'] == 0:
                print("Out off Items.....")
                continue

            player.items[choice_item]['quantity'] -= 1

            if item.types == "potion":
                player.take_heal(item.prop)
                print("Player used ", item.name, "and healed by", item.prop, "HP")

            elif item.types == "elixer":
                if item.name == "MegaElixer":
                    for i in players:
                        i.hp = i.maxhp
                        i.mp = i.maxmp
                    print("All Players Hp/Mp restored")
                else:
                    player.hp = player.maxhp
                    player.mp = player.maxmp
                    print(player.name, "HP/Mp fully restored")

            elif item.types == "attack":
                enemy = player.choose_target(enemies)
                enemies[enemy].take_damage(item.prop)
                print(player.name, "used", item.name, "and enemy lost", item.prop, "HP to", enemies[enemy].name)

                if enemies[enemy].get_hp() == 0:
                    del enemies[enemy]
# =========================================================================================================
# ENEMY PARTx
    print(bcolors.FAIL, bcolors.BOLD, "ENEMY'S TURN", bcolors.ENDC)
    for enemy in enemies:
        target = random.randrange(0, 3)
        x = players[target]
        enemy_damage = enemy.generate_damage()
        x.take_damage(enemy_damage)
        print(enemy.name, "attacked", x.name, "for", enemy_damage)

        defeated_enemies = 0
        for i in enemies:
            if i.get_hp() == 0:
                defeated_enemies += 1
        defeated_players = 0
        for j in players:
            if j.get_hp() == 0:
                defeated_players += 1

        if defeated_enemies == 3:
            print("Players Won")
            running = False

        if defeated_players == 3:
            print("Enemies Won")
            running = False


"""        if enemy1.hp == 0 and enemy2.hp == 0 and enemy3.hp == 0:
            print("Player Win")
            x.players_get_stats()
            running = False

        elif player1.hp == 0 and player3.hp == 0 and player2.hp == 0:
            print("Enemy  Win")
            running = False
"""
        #for enemy in enemies:
