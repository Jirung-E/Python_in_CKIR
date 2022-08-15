from .Character import *
from .Monster import *

import random


class Dungeon:
    def __init__(self, level):
        if level <= 0:
            level = 1
        self.__level = level

    def enterTheDungeon(self): 
        print("You are now Entering Dungeon...", end='')
        print("\n\n\n", end='\n')

        for _ in range(0, random.randrange(5, 10)):
            print("\n\n\n\n\n\n")
            enemy = Monster(random.choice([ 'Slime', 'Rat', 'Wolf', 'Devil', 'Golem' ]), random.randrange(self.__level - 5, self.__level + 10), random.randrange(1000, 2000)) 

            while True:
                print(f"You: Lv.{self.__level} {self.__class} ({self.__exp} / {self.__limit})")
                print(f"       life: {self.__life} \t mana: {self.__mana}")
                print("\n\n\n\n\n\n")
                print(f"                                       Enemy: Lv.{enemy['level']} {enemy['name']}")
                print(f"                                                life: {enemy['life']}")

                print("\n\n")
                print("  1: Attack  |  2: Status  |  Other: Run")
                c = input()
                if c == "1":
                    self.__attack(enemy)
                    if enemy['life'] <= 0:
                        enemy["life"] = 0
                        print(f"You: Lv.{self.__level} {self.__class}")
                        print(f"       life: {self.__life} \t mana: {self.__mana}")
                        print("\n\n\n\n\n\n")
                        print(f"                                       Enemy: Lv.{enemy['level']} {enemy['name']}")
                        print(f"                                                life: {enemy['life']}")

                        print("You win!")
                        xp = enemy["level"] * 5
                        self.expUp(xp)
                        break
                elif c == "2":
                    self.__showStatus()
                else:
                    self.leaveTheDungeon()
                    return
                print("\n\n\n\n")

    def leaveTheDungeon(self):
        print("You are now Leaving Dungeon...", end='')
        print("\n\n\n", end='\n')