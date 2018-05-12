'''
Created on 01.05.2018
@author: Karl
'''
#Imports
from Fighter import Fighter
from Cargo import Cargo
from Agri import Agri
from Industry import Industry
from HighTech import HighTech
import os

#Variables
money = 1000
ships = []
name = None

#Methods
def chooseDest():
    while(True):
        print("Choose your planet!")
        choice = input("Agriculture[1], Industry[2], HighTech[3]")
        if(choice == "1"):
            activePlanet = Agri()
            break
        if(choice == "2"):
            activePlanet = Industry()
            break
        if(choice == "3"):
            activePlanet = HighTech()
            break

        print("Please enter a valid number!")
    return activePlanet

def mainMenu():
    while(True):
        print("Welcome to " + activePlanet.__class__.__name__ + " planet " + activePlanet.getName())
        print("")
        print("What would you like to do?")
        print("[1] Buy ship")
        print("[2] Sell ship")
        print("[3] View own ships")
        print("[4] Buy goods")
        print("[5] Sell goods")
        print("[0] Travel to the next planet")
        choice = 0
        choice = input()
        if(choice == "1"):
            buyShip()
        
def buyShip():
    choice = 0
    print("What would you like to buy?")
    print("[1] Fighter Ship")
    print("[2] Cargo Ship")
    print("[0] Nothing")
    choice = input()
    if(choice == "1" or choice == "2"):
        if(choice == "1"):
            ships.insert(len(ships), Fighter())
            print("You bought a Fighter Ship")
        if(choice == "2"):
            ships.insert(len(ships), Cargo())
            print("Thank you for your purchase!")

    print("You currently have these ships: ")
    cf = 0
    cc = 0
    for s in ships:
        if(s.__class__.__name__ == "Fighter"):
            cf = cf + 1
        else:
            cc = cc + 1
    print(str(cf) + " x Fighter")
    print(str(cc) + " x Cargo")
    input("Press return to accept")
        

#Setup
name = input("Please enter your name: ")
print("Welcome to SpaceSim " + name + "!")
print("Which planet would you like to travel to first? ")
activePlanet = chooseDest()
mainMenu()