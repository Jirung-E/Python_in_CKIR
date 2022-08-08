import random
from .JsonLoader import *

def codeGenerator():
    alphabets = [ 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z' ]
    code = ""
    for i in range(0, 5):
        code = code + random.choice(alphabets)
    return code

class Player:
    def __init__(self):
        self.nickname = "unnamed"
        self.code = codeGenerator()
        self.characters = []

    def load(self, nickname):
        loader = JsonLoader()
        user_info = loader.load(f"src/users/{nickname}.json")
        # 로드 실패시 users폴더에 새로운 플레이어 정보 생성해서 저장하는 기능 구현 필요
        self.nickname = user_info['nickname']
        self.code = user_info['code']
        self.characters = user_info['characters']

    def showInfo(self):
        print("User Info: ")
        print(self.nickname)
        print(self.code)
        for e in self.characters:
            print(e)
