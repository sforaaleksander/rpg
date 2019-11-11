import time
import random
import sys


def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)


class Hero:
    exp_points = 0

    def __init__(self, name, health_points, strength_points, defence_points):
        self.name = name
        self.health_points = health_points
        self.strength_points = strength_points
        self.defense_points = defence_points

    def death(self):
        if self.health_points >= 0:
            print("You are dead!")


Hero1 = Hero("", 100, 0, 0)
Hero1.name = input(delay_print("Welcome to the RPG game! Type in the name of your character: "))
Hero1 = Hero(Hero1.name, 100, 0, 0)

delay_print("Hello " + Hero1.name + "! Time to assign your skill points. "
                        "You have 10 points left. Add points to the following atributes: \nSTRENGTH \nDEFENSE")


Hero1.strength_points = int(input("\nAdd points to strength: "))
spare_points = 10
if Hero1.strength_points > spare_points:
    delay_print("\nYou have only 10 points to assign.")


spare_points = 10 - Hero1.strength_points


Hero1.defence_points = int(input("Add points to defence: "))
if Hero1.defence_points > spare_points:
    delay_print("You have only " + str(spare_points) + " points to assign.")

delay_print(("Well done, %s. You have %d strength points and %d defence points. Let's start the game!" % (Hero1.name,
Hero1.strength_points, Hero1.defence_points)))

time.sleep(4)


class Monster:
    def __init__(self, health_points, strength_points, defence_points):
        self.health_points = health_points
        self.strength_points = strength_points
        self.defence_points = defence_points


Jaszczur = Monster(10, 5, 6)


def fight_monster(monsters_health, monsters_strength, monsters_defence, heroes_health, heroes_strength, heroes_defence):
    delay_print("Fight!")

    keep_on_fighting = True

    while keep_on_fighting:
        if monsters_health <= 0 or heroes_health <= 0:
            keep_on_fighting = False

        delay_print("\nYou attack the monster!")
        attack1 = heroes_strength * random.randint(0, 5) - monsters_defence
        monsters_health -= attack1
        delay_print("\nYou took the monster %d health points!" % attack1)
        delay_print("\nThe monster has %d health points left!" % monsters_health)
        if monsters_health <=0:
            break

        delay_print("\nNow the monster attacks!")
        attack2 = monsters_strength * random.randint(0, 5) - heroes_defence
        heroes_health -= attack2
        delay_print("\nThe monster took you %d health points!" % attack2)
        delay_print("\nYou have %d health points left!" % heroes_health)

    if monsters_health <= 0:
        delay_print("\nYou killed the monster!")
        delay_print("\nYou earned 10 EXP points!")
        Hero1.exp_points += 10
    elif heroes_health <= 0:
        delay_print("\nYou are dead!")


def yes_or_no():
    param = random.randint(0,1)
    if param == 1:
        return True
    return False


def run():
    delay_print("\nYou are running! The monster is right behind you...")
    delay_print("\nCan you make it?")
    delay_print("\n......")
    delay_print("\nPray for your soul...!")
    if yes_or_no():
        delay_print("\nYou made it!")
    elif not yes_or_no():
        delay_print("\nThe monster got you! Prepare for the fight!")
        fight_monster(Jaszczur.health_points, Jaszczur.strength_points, Jaszczur.defence_points, Hero1.health_points,
                      Hero1.strength_points, Hero1.defence_points)


choice = input(delay_print("\nSuddenly a monster attacks you! Do you want to FIGHT or RUN?"))
choice.lower()
if choice == "run":
    run()
elif choice == "fight":
    fight_monster(Jaszczur.health_points, Jaszczur.strength_points, Jaszczur.defence_points, Hero1.health_points,
                  Hero1.strength_points, Hero1.defence_points)


def wise_man():
    delay_print("\nYou encountered an old, wise man. Thanks to his wisdom, you gained 3 skill points. "
                "\nDo you want to add them to STRENGTH or DEFENCE?")
    wisdom = input("\nType in STRENGTH or DEFENCE to spend your points: ")
    wisdom.lower()
    if wisdom == "strength":
        Hero1.strength_points += 3
        delay_print("\nYou now have %d strength points!" % Hero1.strength_points)
    elif wisdom == "defence":
        Hero1.defence_points += 3
        delay_print("\nYou now have %d defence points!" % Hero1.defence_points)


wise_man()

delay_print("\nTake some rest, soldier, you did well today. The journey will continue tomorrow.")