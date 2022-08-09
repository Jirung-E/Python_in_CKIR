from .JsonManager import *

class Users:
    def __init__(self):
        self.users = self.loadInfo()

    def loadInfo(self):
        loader = JsonManager()
        return loader.load("users/users.json")['users']

    def get(self):
        return self.users