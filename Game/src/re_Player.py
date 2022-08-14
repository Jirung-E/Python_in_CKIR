import json

from .Users import *


class re_Player:
    def __init__(self, nickname):
        self.__nickname = nickname
        self.__data = {}

        self._users = Users()

        self.__path = f"json/users/{nickname}.json"

        self.__load()
        self.__set()
        self.__save()

    def __del__(self):
        self.__save()


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
        with open(self.__path, 'w') as outfile:
            json.dump(self.__data, outfile, indent=4)

    def __makeCode(self):
        return f"#{len(self._users.get()) + 1}"