from src.Player import *
from src.Users import *
from src.Character import *

from src.re_Player import *


def test():
    users = Users().get()
    print(users)

    p = []
    for e in users:
        p.append(Player(e))

    for e in p:
        e.showInfo()
        print()

    p[1].makeNewCharacter(random.choice(["Archer", "Warrior", "Mage", "Assassin"]))
    p[1].showInfo()

    for i in range(4, 10):
        p[1].deleteCharacter(i)
    p[1].showInfo()

def characterTest():
    ch = Character("Assassin")
    ch.showInfo()
    ch.expUp(50000)
    for i in range(0, ch.getLevel() * 3):
        ch.statusUp("str")
        ch.statusUp("dex")
        ch.statusUp("def")
        ch.statusUp("int")
        ch.statusUp("agi")
    ch.showInfo()

def playerCharacterTest():
    p = Player("Nick")
    p.selectCharacter(0).showInfo()
    p.selectCharacter(1).showInfo()

# playerCharacterTest()
# characterTest()
# test()

def testUsers():
    users = Users()
    print(users.getNumOfUsers())
    print(users.get())
    users.add("Abraham")
    print(users.getNumOfUsers())
    print(users.get())

# testUsers()

def testRePlayer():
    rp = re_Player("Kevin")
    n = re_Player("Nguyen")

testRePlayer()