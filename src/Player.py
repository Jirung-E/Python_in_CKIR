import random
import json

def _codeGenerator():
    alphabets = [ 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z' ]
    code = "#"
    for i in range(0, 8):
        code = code + random.choice(alphabets)
    return code

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