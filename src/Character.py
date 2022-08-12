class Character:
    def __init__(self, _class):
        self.__class = _class

        self.__exp = 0
        self.__level = 0
        self.__limit = 50
        self.__limit_increase_per_level = 5

        self.status = {
            "str": 0,               # 물리 공격력, 체력
            "def": 0,               # 방어력, 체력
            "int": 0,               # 마법 공격력, 마나
            "dex": 0,               # 치명타율, 공격 속도
            "agi": 0                # 회피율, 이동 속도
        }
        self.skill_point = 0
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

#public member functions
    def statusUp(self, stat):
        if self.skill_point > 0:
            self.status[stat] = self.status[stat] + 1
            self.skill_point = self.skill_point - 1
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
        print(f"    str: {self.status['str']} \t\t | \t strength:    {self.__strength} \t atk_per_sec: {self.__atk_per_sec}")
        print(f"    def: {self.status['def']} \t\t | \t life:        {self.__life} \t critical:    {self.__critical}")
        print(f"    int: {self.status['int']} \t\t | \t defence:     {self.__defence} \t dodge:       {self.__dodge}")
        print(f"    dex: {self.status['dex']} \t\t | \t inteligence: {self.__inteligence} \t movement:    {self.__movement}")
        print(f"    agi: {self.status['agi']} \t\t | \t mana:        {self.__mana}")
        print(f"  skiil point: {self.skill_point}")

#private member functions
    def __levelUp(self):
        self.__level = self.__level + 1
        self.__limit = self.__limit + self.__limit_increase_per_level
        self.skill_point = self.skill_point + self.__sp_per_level
        print("Level Up!")

    def __update(self):
        self.__strength = self.status["str"] * 2.0
        self.__life = self.status["str"] * 1.0 + self.status["def"] * 1.5
        self.__defence = self.status["def"] * 2.0
        self.__inteligence = self.status["int"] * 2.0
        self.__mana = self.status["int"] * 1.5
        self.__atk_per_sec = 1 + self.status["dex"] * 0.05
        self.__critical = self.status["dex"] * 0.5
        if self.__dodge > 100:
            self.__dodge = 100
        self.__dodge = self.status["agi"] * 0.5
        if self.__dodge > 100:
            self.__dodge = 99.9
        self.__movement = 1 + self.status["agi"] * 0.01