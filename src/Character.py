class Character:
    def __init__(self):
        self.__exp = 0
        self.__level = 0
        self.__limit = 50
        self.status = {
            "str": 0,
            "def": 0,
            "int": 0,
            "dex": 0,
            "agi": 0
        }
        self.skill_point = 0
        self.__sp_per_level = 3

    def __levelUp(self):
        self.__level = self.__level + 1
        self.__limit = self.__limit + 10
        self.skill_point = self.skill_point + self.__sp_per_level
        print("Level Up!")
        self.showLevel()
        self.showSp()

    def getExp(self, exp):
        self.__exp = self.__exp + exp
        while self.__exp > self.__limit:
            self.__levelUp()
            self.__exp = self.__exp - self.__limit

    def showLevel(self):
        print(self.__level)

    def showSp(self):
        print(self.skill_point)