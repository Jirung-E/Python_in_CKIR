import json

class Character:
    def __init__(self, _class = None):
        self.__class = _class

        self.__exp = 0
        self.__level = 1
        self.__limit = 50
        self.__limit_increase_per_level = 5

        self.__status = {
            "str": 1,               # 물리 공격력, 체력
            "def": 1,               # 방어력, 체력
            "int": 1,               # 마법 공격력, 마나
            "dex": 1,               # 치명타율, 공격 속도
            "agi": 1                # 회피율, 이동 속도
        }
        self.__skill_point = 0
        self.__sp_per_level = 3

        self.__strength = 0
        self.__life = 0
        self.__defence = 0
        self.__inteligence = 0
        self.__mana = 0
        self.__atk_per_sec = 0
        self.__critical = 0
        self.__dodge = 0
        self.__movement = 0

        self.__update()

#public member functions
    def statusUp(self, stat):
        if self.__skill_point > 0:
            self.__status[stat] = self.__status[stat] + 1
            self.__skill_point = self.__skill_point - 1
        self.__update()

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
        print(f"    str: {self.__status['str']} \t\t | \t strength:    {self.__strength} \t atk_per_sec: {self.__atk_per_sec}")
        print(f"    def: {self.__status['def']} \t\t | \t life:        {self.__life} \t critical:    {self.__critical}")
        print(f"    int: {self.__status['int']} \t\t | \t defence:     {self.__defence} \t dodge:       {self.__dodge}")
        print(f"    dex: {self.__status['dex']} \t\t | \t inteligence: {self.__inteligence} \t movement:    {self.__movement}")
        print(f"    agi: {self.__status['agi']} \t\t | \t mana:        {self.__mana}")
        print(f"  skiil point: {self.__skill_point}")

    def getStatus(self):
        return self.__status

    def _load(self, data):
        self.__class = data["class"]
        self.__level = data["level"]
        self.__limit = self.__limit + self.__limit_increase_per_level * (self.__level - 1)
        self.__status['str'] = data["status"]["str"]
        self.__status['def'] = data["status"]["def"]
        self.__status['int'] = data["status"]["int"]
        self.__status['dex'] = data["status"]["dex"]
        self.__status['agi'] = data["status"]["agi"]
        self.__skill_point = 5 + (self.__level - 1) * 3 - (self.__status['str'] + self.__status['def'] + self.__status['int'] + self.__status['dex'] + self.__status['agi']) # 5:기본 포인트
        self.__update()
        return self

#private member functions
    def __levelUp(self):
        self.__level = self.__level + 1
        self.__limit = self.__limit + self.__limit_increase_per_level
        self.__skill_point = self.__skill_point + self.__sp_per_level
        print("Level Up!")

    def __update(self):
        self.__strength = self.__status["str"] * 2.0
        self.__life = self.__status["str"] * 6.0 + self.__status["def"] * 9.0
        self.__defence = self.__status["def"] * 2.0
        self.__inteligence = self.__status["int"] * 2.0
        self.__mana = self.__status["int"] * 9.0
        self.__atk_per_sec = 1 + self.__status["dex"] * 0.01
        self.__critical = self.__status["dex"] * 0.5
        if self.__dodge > 100:
            self.__dodge = 100
        self.__dodge = self.__status["agi"] * 0.5
        if self.__dodge > 100:
            self.__dodge = 99.9
        self.__movement = 1 + self.__status["agi"] * 0.01