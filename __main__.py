from functions import *
from classes import *

sayHello()
sayHelloTo("Jir")

menu = Menu()
print(f"{menu.getRandom()} 어떰?")
cmenu = ChineseFood()
print(f"{cmenu.getRandom()} 어떰?")

dinner = StreetFood()
print(f"{dinner.getRandom()} 먹고", end = ' ')
dinner = Dessert()
print(f"후식 {dinner.getRandom()}", end = '\n')