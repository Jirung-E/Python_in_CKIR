import time
import random

class Character:
    def __init__(self, _class = None):
        self.__class = _class

        self.__exp = 0
        self.__level = 1
        self.__limit = 50
        self.__limit_increase_per_level = 5

        self.__stats = {
            "str": 1,               # 물리 공격력, 체력
            "def": 1,               # 방어력, 체력
            "int": 1,               # 마법 공격력, 마나
            "dex": 1,               # 치명타율, 공격 속도
            "agi": 1                # 회피율, 이동 속도
        }
        self.__skill_point = 0
        self.__sp_per_level = 3

        self.__strength = 0
        self.__life_max = 0
        self.__life = 0
        self.__defence = 0
        self.__inteligence = 0
        self.__mana_max = 0
        self.__mana = 0
        self.__atk_per_sec = 0
        self.__critical = 0
        self.__dodge = 0
        self.__movement = 0

        self.__update()

#public member functions
    def statUp(self, stat):
        if stat not in [ "str", "def", "int", "dex", "agi" ]:
            return False
        if self.__skill_point > 0:
            self.__stats[stat] = self.__stats[stat] + 1
            self.__skill_point = self.__skill_point - 1
        self.__update()
        return True

    def expUp(self, exp):
        self.__exp = self.__exp + exp
        while self.__exp > self.__limit:
            self.__levelUp()
            self.__exp = self.__exp - self.__limit

    def getLevel(self):
        return self.__level

    def showInfo(self):
        print(f"class: {self.__class}")
        print(f"  level: {self.__level}")
        print(f"  exp:   {self.__exp}")
        print("  status: ")
        print(f"    str: {self.__stats['str']} \t\t | \t life:        {self.__life_max} / {self.__life_max} \t mana:        {self.__mana_max} / {self.__mana_max}")
        print(f"    def: {self.__stats['def']} \t\t | \t strength:    {self.__strength} \t inteligence: {self.__inteligence}")
        print(f"    int: {self.__stats['int']} \t\t | \t defence:     {self.__defence} \t atk_per_sec: {self.__atk_per_sec}")
        print(f"    dex: {self.__stats['dex']} \t\t | \t critical:    {self.__critical} \t dodge:       {self.__dodge}")
        print(f"    agi: {self.__stats['agi']} \t\t | \t movement:    {self.__movement}")
        print(f"  skiil point: {self.__skill_point}")

    def showSimpleInfo(self):
        print(f"{self.__class} ({self.__level}) / str: {self.__stats['str']} def: {self.__stats['def']} int: {self.__stats['int']} dex: {self.__stats['dex']} agi: {self.__stats['agi']} ")

    def getStats(self):
        return self.__stats

    def getData(self):
        data = {}
        data["class"] = self.__class
        data["level"] = self.__level
        data["exp"] = self.__exp
        data["stats"] = self.__stats

        return data

    def getStatus(self):
        data = {}
        data["class"] = self.__class
        data["level"] = self.__level
        data["exp"] = self.__exp
        data["limit"] = self.__limit
        data["stats"] = self.__stats
        data["skill_point"] = self.__skill_point
        data["life_max"] = self.__life_max
        data["life"] = self.__life
        data["mana_max"] = self.__mana_max
        data["mana"] = self.__mana

        return data

    def attack(self, enemy):
        damage = self.__strength + self.__inteligence

        cri = random.choices([True, False], weights=(self.__critical, 100 - self.__critical))[0]
        if cri is True:
            damage = damage * 2
            print("Critical!")
            
        enemy.attackedBy(self)
        print("-" + str(damage))

    def attackedBy(self, enemy):
        damage = enemy.__strength + enemy.__inteligence

        cri = random.choices([True, False], weights=(enemy.__critical, 100 - enemy.__critical))[0]
        if cri is True:
            damage = damage * 2
            print("Critical!")
            
        self.__life = self.__life - damage
        if self.__life <= 0:
            self.__life = 0
        print("-" + str(damage))

    def _load(self, data):
        self.__class = data["class"]
        self.__level = data["level"]
        self.__limit = self.__limit + self.__limit_increase_per_level * (self.__level - 1)
        self.__exp = data["exp"]
        self.__stats['str'] = data["stats"]["str"]
        self.__stats['def'] = data["stats"]["def"]
        self.__stats['int'] = data["stats"]["int"]
        self.__stats['dex'] = data["stats"]["dex"]
        self.__stats['agi'] = data["stats"]["agi"]
        self.__skill_point = 5 + (self.__level - 1) * 3 - (self.__stats['str'] + self.__stats['def'] + self.__stats['int'] + self.__stats['dex'] + self.__stats['agi']) # 5:기본 포인트
        self.__update()
        return self

#private member functions
    def __levelUp(self):
        self.__level = self.__level + 1
        self.__limit = self.__limit + self.__limit_increase_per_level
        self.__skill_point = self.__skill_point + self.__sp_per_level
        print("Level Up!")

    def __update(self):
        self.__strength = self.__stats["str"] * 2.0
        self.__life_max = self.__stats["str"] * 6.0 + self.__stats["def"] * 9.0
        self.__life = self.__life_max
        self.__defence = self.__stats["def"] * 2.0
        self.__inteligence = self.__stats["int"] * 2.0
        self.__mana_max = self.__stats["int"] * 9.0
        self.__mana = self.__mana_max
        self.__atk_per_sec = 1 + self.__stats["dex"] * 0.01
        self.__critical = self.__stats["dex"] * 0.5
        if self.__dodge > 100:
            self.__dodge = 100
        self.__dodge = self.__stats["agi"] * 0.5
        if self.__dodge > 100:
            self.__dodge = 99.9
        self.__movement = 1 + self.__stats["agi"] * 0.01