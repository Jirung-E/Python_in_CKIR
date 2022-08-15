import json

from .Users import *
from .Character import *


class Player:
# constructor
    def __init__(self, nickname):
        self.__nickname = nickname
        self.__data = {}
        self.character = {}
        self.__char_index = None

        self._users = Users()

        self.__path = f"json/users/{nickname}.json"

        self.__load()
        self.__set()
        self.__save()

# destructor
    def __del__(self):
        self.__save()


# private member functions
    def showInfo(self):
        print("User Info: " + self.__nickname)
        print("    " + self.__data["code"])
        print("    characters:")
        cnt = 1
        for e in self.__data["characters"]:
            c = Character()
            c._load(e)
            print(f"        {cnt}: ", end = '')
            c.showSimpleInfo()
            cnt = cnt + 1

    def makeNewCharacter(self, character_class):
        c = Character(character_class)
        char = { "class": character_class, "level": c.getLevel(), "exp": 0, "status": c.getStatus() }
        self.__data["characters"].append(char)

    def deleteCharacter(self, index):
        if index >= len(self.__data["characters"]) or index < 0:
            print("?")
            return
        else :
            del self.__data["characters"][index]
            print("deleted")

    def selectCharacter(self, index):
        self.character = Character()._load(self.__data["characters"][index])
        self.__char_index = index

    def getNumberOfCharacters(self):
        return len(self.__data["characters"])


# private member functions
    def __load(self):
        try:
            file = open(self.__path, 'r')
        except:
            self.__make(self.__nickname)
            file = open(self.__path, 'r')
        
        content = file.read()
        file.close()
        self.__data = json.loads(content)

    def __set(self):
        self.nickname = self.__data['nickname']
        
    def __make(self, nickname):
        self.__data['nickname'] = nickname
        self.__data['code'] = self.__makeCode()
        self.__data['characters'] = []
        self.__save()
        self._users.add(nickname)

    def __save(self):
        if self.__char_index is not None:
            self.__data["characters"][self.__char_index] = self.character.getData()
        with open(self.__path, 'w') as outfile:
            json.dump(self.__data, outfile, indent=4)

    def __makeCode(self):
        return f"#{len(self._users.get()) + 1}"