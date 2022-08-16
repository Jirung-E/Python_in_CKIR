from os import stat_result
from .Character import *


class Monster(Character):
    def __init__(self, _class, level=None):
        super().__init__(_class)
        if level is not None:
            if level <= 0:
                level = 1
            self.__level = level

        self.monster_list = [
            "Slime", "Rat", "Wolf", "Devil", "Golem"
        ]

    def summon(self, level):
        mon = self.getData()["class"]
        if mon not in self.monster_list:
            raise Exception(f"Monster doesn't have member {mon}")
        else:
            if mon == "Slime":
                return Slime(level)
            elif mon == "Rat":
                return Rat(level)
            elif mon == "Wolf":
                return Wolf(level)
            elif mon == "Devil":
                return Devil(level)
            elif mon == "Golem":
                return Golem(level)
        


class Slime(Monster):
    def __init__(self, level):
        super().__init__("Slime", level)
        for _ in range(0, level * 3):
            self.statUp("str")
            self.statUp("def")
            self.statUp("int")
            self.statUp("dex")
            self.statUp("agi")

class Rat(Monster):
    def __init__(self, level):
        super().__init__("Rat", level)
        for _ in range(0, level * 3):
            self.statUp("str")
            self.statUp("def")
            self.statUp("int")
            self.statUp("dex")
            self.statUp("agi")


class Wolf(Monster):
    def __init__(self, level):
        super().__init__("Wolf", level)
        for _ in range(0, level * 3):
            self.statUp("str")
            self.statUp("def")
            self.statUp("int")
            self.statUp("dex")
            self.statUp("agi")

class Devil(Monster):
    def __init__(self, level):
        super().__init__("Devil", level)
        for _ in range(0, level * 3):
            self.statUp("str")
            self.statUp("def")
            self.statUp("int")
            self.statUp("dex")
            self.statUp("agi")

class Golem(Monster):
    def __init__(self, level):
        super().__init__("Golem", level)
        for _ in range(0, level * 3):
            self.statUp("str")
            self.statUp("def")
            self.statUp("int")
            self.statUp("dex")
            self.statUp("agi")