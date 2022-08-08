import random

class Menu:
    def __init__(self):
        self.menu = [
            "삼겹살",
            "족발",
            "보쌈",
            "치킨",
        ]

    def getRandom(self):
        return random.choice(self.menu)

class ChineseFood(Menu):
    def __init__(self):
        self.menu = [
            "짜장면",
            "짬뽕",
            "탕수육",
            "깐풍기",
        ]

class StreetFood(Menu):
    def __init__(self):
        self.menu = [
            "떡볶이",
            "김밥",
            "라면",
            "순대",
        ]

class Dessert(Menu):
    def __init__(self):
        self.menu = [
            "커피",
            "빙수",
            "슬러시",
            "케이크",
            "안먹어!",
        ]