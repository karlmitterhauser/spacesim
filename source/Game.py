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

#Variables
money = 1000
ships = []
name = None

#Methods
def chooseDest():
    while(True):
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

#Setup
name = input("Please enter your name: ")
print("Welcome to SpaceSim " + name + "!")
print("Which planet would you like to travel to first? ")
activePlanet = chooseDest()

#Main Menu
print("Welcome to " + activePlanet.getType) + " planet " + activePlanet.getName())


choice = 0 
if(choice == 1 or choice == 2):
    if(choice == 1):
        ships.insert(len(ships), Fighter())
        print("You bought a Fighter Ship")
        if(choice == 2):
            ships.insert(len(ships), Cargo())
    print("You bought a Cargo Ship")

    print("You currently have these ships: ")
    cf = 0
    cc = 0
    for s in ships:
        if(s.getType() == "Fighter"):
            cf = cf + 1
        else:
            cc = cc + 1
        print(str(cf) + " x Fighter")
        print(str(cc) + " x Cargo")
        


'''
#Test for the planet Mechanics
myPlanetA = Agri()
print('Agriculture Planet = ' +myPlanetA.getName())
pricel = myPlanetA.getPrices()
for key,value in pricel.items():
print('Price of ' +key+ ' is ' ,value)
    
myPlanetB = Industry()
print('Industry Planet = ' +myPlanetB.getName())
pricel = myPlanetB.getPrices()
for key,value in pricel.items():
print('Price of ' +key+ ' is ' ,value)
    
myPlanetC = HighTech()
print('HighTech Planet = ' +myPlanetC.getName())
pricel = myPlanetC.getPrices()
for key,value in pricel.items():
print('Price of ' +key+ ' is ' ,value)
'''