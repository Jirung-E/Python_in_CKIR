from src.Player import *
from src.Users import *

# player = Player("Nick")
# player.showInfo()


users = Users().get()
print(users)

p = []
for e in users:
    p.append(Player(e))

for e in p:
    e.showInfo()
    print()

p[1].makeNewCharacter("Archer")
p[1].showInfo()

for i in range(4, 10):
    p[1].deleteCharacter(i)
p[1].showInfo()