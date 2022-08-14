import json


class Users:
# constructor
    def __init__(self):
        self.__path = "json/users/users.json"
        self.__data = None
        self.__users = None

        self.__load()
        self.__set()
        self.__save()

# destructor
    def __del__(self):
        self.__save()


# public member functions
    def get(self):
        return self.__users

    def getNumOfUsers(self):
        return len(self.__users)

    def add(self, nickname):
        for e in self.__users:
            if e == nickname:
                return
        self.__users.append(nickname)
        self.__save()

# private member functions
    def __load(self):
        file = open(self.__path, 'r')
        content = file.read()
        file.close()
        self.__data = json.loads(content)

    def __set(self):
        self.__users = self.__data["users"]

    def __save(self):
        self.__data["users"] = self.__users
        with open(self.__path, 'w') as outfile:
            json.dump(self.__data, outfile, indent=4)
