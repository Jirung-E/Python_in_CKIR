from .Character import *
from .Monster import *

import random


class Dungeon:
    def __init__(self, level):
        if level <= 0:
            level = 1
        self.__level = level

    def enterTheDungeon(self, character : Character): 
        print("You are now Entering Dungeon...", end='')
        print("\n\n\n", end='\n')

        for _ in range(0, random.randrange(5, 10)):
            print("\n\n\n\n\n\n")
            monster = Monster(random.choice([ 'Slime', 'Rat', 'Wolf', 'Devil', 'Golem' ])) 
            monster.summon(random.randrange(self.__level - 5, self.__level + 10))

            while True:
                char_data = character.getStatus()
                mons_data = monster.getStatus()
                self.__showGameScreen(char_data, mons_data)

                print("\n\n")
                print("  1: Attack  |  2: Status  |  Other: Run")
                c = input()
                if c == "1":
                    character.attack(monster)
                    mons_data = monster.getStatus()
                    if mons_data["life"] <= 0:
                        mons_data["life"] = 0
                        self.__showGameScreen(char_data, mons_data)

                        print("You win!")
                        xp = mons_data["level"] * 5
                        character.expUp(xp)
                        break
                elif c == "2":
                    self.__showStatus(character)
                else:
                    self.leaveTheDungeon()
                    return
                print("\n\n\n\n")

    def leaveTheDungeon(self):
        print("You are now Leaving Dungeon...", end='')
        print("\n\n\n", end='\n')


    def __showGameScreen(self, char_data, mons_data):
        print(f"You: Lv.{char_data['level']} {char_data['class']} ({char_data['exp']} / {char_data['limit']})")
        print(f"       life: {char_data['life']} / {char_data['life_max']} \t mana: {char_data['mana']} / {char_data['mana_max']}")
        print("\n\n\n\n\n\n")
        print(f"                                       Enemy: Lv.{mons_data['level']} {mons_data['class']}")
        print(f"                                                life: {mons_data['life']} / {mons_data['life_max']} \t mana: {mons_data['mana']} / {mons_data['mana_max']}")

    def __showStatus(self, character: Character):
        while True:
            print(character.__stats)
            print("  1: Increase  |  2: Detail  |  Other: exit")
            c = input()
            if c == "1":
                print(f"skill points: {character.getStatus()['skill_point']}")
                print("  str  def  int  dex  agi      (enter 'c' to cancel)")
                st = input()
                if st == 'c':
                    continue
                if character.statUp(st) == True:
                    print("Complete.")
                    continue
                else:
                    print("No such stat.")
                    continue
            elif c == "2":
                character.showInfo()
            else:
                break