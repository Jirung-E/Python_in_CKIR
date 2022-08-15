from os import stat_result
from .Character import *


class Monster(Character):
    def __init__(self, level):
        super.__init__()
        if level <= 0:
            level = 1
        self.__level = level


class Slime(Monster):
    def __init__(self, level):
        super.__init__(level)
        for e in self.__status:
            e["str"] = e["str"] + 1
            e["def"] = e["def"] + 1
            e["int"] = e["int"] + 1
            e["dex"] = e["dex"] + 1
            e["agi"] = e["agi"] + 1