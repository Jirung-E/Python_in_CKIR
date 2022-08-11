import random
import json

def _codeGenerator():
    alphabets = [ 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '2', '3', '4', '5', '6', '7', '8', '9' ]
    code = "#"
    for i in range(0, 8):
        code = code + random.choice(alphabets)
    return code


class Character:
    def __init__(self, character_class):
        self.character_class = character_class
        self.level = 0
        self.status = { "str": 0, "def": 0, "int":0, "dex":0, "agi": 0 }

    def get(self):
        char = { "class": self.character_class, "level": self.level, "status": self.status }
        return char

class Player:
    def __init__(self, nickname):
        self.nickname = ""
        self.code = ""
        self.characters = []

        self.__data = {}

        self.__path = f"json/users/{nickname}.json"

        self.__load(nickname)
        self.__set()

    def __del__(self):
        self.__save()
        pass

    # public member functions
    def showInfo(self):
        print("User Info: " + self.nickname)
        print("    " + self.code)
        print("    characters:")
        for e in self.characters:
            print("        ", end = '')
            print(e, end = '\n')

    def makeNewCharacter(self, character_class):
        self.characters.append(Character(character_class).get())

    # private member functions
    def __load(self, nickname):
        try:
            file = open(self.__path, 'r')
        except:
            self.__make(nickname)
            file = open(self.__path, 'r')
        
        content = file.read()
        file.close()
        self.__data = json.loads(content)

    def __set(self):
        self.nickname = self.__data['nickname']
        self.code = self.__data['code']
        self.characters = self.__data['characters']
        
    def __make(self, nickname):
        self.__data['nickname'] = nickname
        self.__data['code'] = _codeGenerator()
        self.__data['characters'] = []
        self.__save()

    def __save(self):
        with open(self.__path, 'w') as outfile:
            json.dump(self.__data, outfile, indent=4)
