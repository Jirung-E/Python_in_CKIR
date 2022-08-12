from src.Player import *
from src.Users import *
from src.Character import *

# player = Player("Nick")
# player.showInfo()

def test():
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

# test()

def characterTest():
    ch = Character()
    ch.getExp(5000)

characterTest()