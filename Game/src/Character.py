import time
import random

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

    def showSimpleInfo(self):
        print(f"{self.__class} ({self.__level}) / str: {self.__status['str']} def: {self.__status['def']} int: {self.__status['int']} dex: {self.__status['dex']} agi: {self.__status['agi']} ")

    def getStatus(self):
        return self.__status

    def getData(self):
        data = {}
        data["class"] = self.__class
        data["level"] = self.__level
        data["exp"] = self.__exp
        data["status"] = self.__status
        return data

    def enterTheDungeon(self, level=None):
        if level == None:
            level = self.__level
            
        print("You are now Entering Dungeon", end = '')
        for i in range(0, 3):
            # time.sleep(1)
            print(end = '.')
        print("\n\n", end = '\n')

        for i in range(0, random.randrange(5, 10)):
            print("\n\n\n\n\n\n")
            enemy = { 
                "name": random.choice([ 'Slime', 'Rat', 'Wolf' ]), 
                "level": random.randrange(level - 5, level + 10), 
                "life": random.randrange(1000, 2000) }
            if enemy["level"] <= 0:
                enemy["level"] = 1

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
        print("You are now Leaving Dungeon", end = '')
        for i in range(0, 3):
            # time.sleep(1)
            print(end = '.')
        print(end = '\n')

    def _load(self, data):
        self.__class = data["class"]
        self.__level = data["level"]
        self.__limit = self.__limit + self.__limit_increase_per_level * (self.__level - 1)
        self.__exp = data["exp"]
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

    def __attack(self, enemy):
        damage = self.__strength + self.__inteligence

        cri = random.choices([True, False], weights=(self.__critical, 100 - self.__critical))[0]
        if cri is True:
            damage = damage * 2
            print("Critical!")
            
        enemy['life'] = enemy['life'] - damage
        print("-" + str(damage))

    def __showStatus(self):
        while True:
            print(self.__status)
            print("  1: Increase  |  2: Detail  |  Other: exit")
            c = input()
            if c == "1":
                print(f"skill points: {self.__skill_point}")
                st = input()
                self.statusUp(st)
            elif c == "2":
                self.showInfo()
            else:
                break