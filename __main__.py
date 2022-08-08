from src.functions import *
from src.classes import *
from src.JsonLoader import *

sayHello()
sayHelloTo("Jir")

menu = random.choice([Menu(), ChineseFood(), StreetFood()])
dinner = menu.getRandom()
print(f"{dinner} 어떰?")
print(f"{dinner} 먹고", end = ' ')
print(f"후식 {Dessert().getRandom()}?", end = '\n')
print(random.choice(["개별론데;", "ㄱㄱ"]))

loader = JsonLoader()
user_info = loader.load("json/user_info.json")
loader.show()

print(user_info['nickname'])
print(user_info['code'])
print(user_info['characters'][0])
print(user_info['characters'][1])