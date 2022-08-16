from .Player import *
from .Monster import *
from .Users import *
from .Dungeon import *


class GameManager:
    def __init__(self):
        self.__player = None

    def signIn(self):
        while True:
            print("------------------------------ [ Sign In ] ------------------------------")
            print("Enter Your Nickname: ", end='')
            nickname = input()
            for e in Users().get():
                if e == nickname:
                    print(f"Welcome {nickname}!", end='\n')
                    self.__player = Player(nickname)
                    return True

            print("We don\'t have any data of you. ", end='\n')

            while True:
                print("1. Try Again        2. Sign Up        3. Exit")
                print(": ", end='')
                key = input()
                print("\n\n\n", end='\n')
                if key == "1":
                    print("Try Again....")
                    break
                elif key == "2":
                    self.signUp()
                    break
                elif key == "3":
                    print("Bye.")
                    return False
                else:
                    print("Invalid input. Please enter a valid number")

        return False

    def signUp(self):
        print("------------------------------ [ Sign Up ] ------------------------------")
        print("Nickname: ", end='')
        nickname = input()

        print("Creating new user...")
        users = Users()
        users.add(nickname)

        print("Complete.\n\n\n")


    def playGame(self):
        if self.signIn() == False:
            print("...")
            return

        while True:
            print("\n\n\n\n\n\n\n\n\n\n")
            print("------------------------------ [ User Info ] ------------------------------")
            self.__player.showInfo()
            print("\n\n\n")

            print("1. Play        2. Make new character        Other: Exit")
            print(": ", end='')
            key = input()
            print("\n\n\n", end='\n')

            if key == "1":
                if self.__player.getNumberOfCharacters() == 0:
                    print("You can\'t play.")
                    print("You need to make a character first!")
                    continue
                else:
                    while True:
                        print("Choose a character to play (enter \'c\' to cancel)")
                        print(": ", end='')
                        index = input()
                        print("\n\n\n", end='\n')

                        if index == 'c':
                            break

                        try:
                            self.__player.selectCharacter(int(index)-1)
                        except:
                            print(f"Please enter a value between \'1\' ~ \'{self.__player.getNumberOfCharacters()}\'")
                            continue

                        self.__player.character.enterTheDungeon()

            elif key == "2":
                print("Choose class of your character")
                while True:
                    print("  Warrior    Archer    Mage    Assassin    (enter \'c\' to cancel)")
                    print(": ", end='')
                    cls = input()
                    print("\n\n\n", end='\n')
                    if cls == 'c':
                        break

                    if cls not in [ "Warrior", "Archer", "Mage", "Assassin" ]:
                        print("Invalid input.")
                        print("Please enter the correct class name.")
                        continue
                    self.__player.makeNewCharacter(cls)
                    print("Complete!")
            else:
                print("Bye!")
                break
