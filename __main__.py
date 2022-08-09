from src.Player import *
from src.Users import *

player = Player()
player.load("Nick")
player.showInfo()


users = Users().get()
print(users)

p = []
p.append(Player())
p.append(Player())
p[1].load(users[1])
p[1].showInfo()