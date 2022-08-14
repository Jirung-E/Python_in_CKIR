from .Character import *


class Monster(Character):
    def __init__(self, race, level, life, damage):
        super.__init__()
        self.__class = race
        self.__level = level
        self.__life = life
        
        self.__damage = damage