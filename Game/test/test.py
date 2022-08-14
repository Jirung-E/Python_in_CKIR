from src.Player import *
from src.Users import *

def testUsers():
    users = Users()
    print(users.getNumOfUsers())
    print(users.get())
    users.add("Abraham")
    print(users.getNumOfUsers())
    print(users.get())

def testPlayer():
    rp = Player("Kevin")

    rp.makeNewCharacter("Warrior")
    rp.showInfo()

    rp.selectCharacter(0)
    rp.character.showInfo()
    rp.character.expUp(8000)
    for i in range(1, 100):
        rp.character.statusUp("str")
        rp.character.statusUp("dex")
    rp.character.showInfo()