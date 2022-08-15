from .Player import *
from .Monster import *
from .Users import *


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
            print("------------------------------ [ User Info ] ------------------------------")
            self.__player.showInfo()
            print("\n\n\n")

            print("1. Play        2. Make new character        Other: Exit")
            key = input()
            if key == "1":
                if self.__player.getNumberOfCharacters() == 0:
                    print("make first")
                    pass
                else:
                    print("Choose a character to play")
                    print(": ", end='')
                    index = int(input())
                    print("\n\n\n", end='\n')

                    self.__player.selectCharacter(index-1)
                    self.__player.character.enterTheDungeon()
            elif key == "2":
                print("Choose class of your character")
                print("  Warrior    Archer    Mage    Assassin")
                print(": ", end='')
                cls = input()
                print("\n\n\n", end='\n')
                self.__player.makeNewCharacter(cls)
                print("Complete!")
            else:
                print("Bye!")
                break
