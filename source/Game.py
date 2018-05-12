'''
Created on 01.05.2018
@author: Karl,Klaus
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
wares = {'wheat' : 0, 'iron': 0, 'phone': 0}
name = None


#Methods

def cargoSpaceCalk():
    '''
    Adds the CargoSpace of all the different cargoships and returns the total
    CargoSpace
    '''
    space = 0;
    for s in ships:
        if(s.__class__.__name__ == "Cargo"):
            space += s.getCargoSpace()
    return space

def sellGoods(): 
    '''
    A function that sells the goods the player owns and adds the value of the 
    sold good to the total amount of money.
    '''
    #variables
    global wares
    global money
    prices = activePlanet.getPrices()
    #function
    print("The selling prices are as followed")
    for key,value in prices.items():
        print(key +": " + str(value))
    ichoice = input("What do you want to sell: wheat[1], iron[2] or phones[3]?")
    number = int(input("How many do you want to sell?"))
    if(ichoice == "1"):
        if(wares['wheat'] >= number):
            money = money + (prices['wheat'] * number)
            wares['wheat'] = wares['wheat'] - number
    if(ichoice == "2"):
        if(wares['iron'] >= number):
            money = money + (prices['iron'] * number)
            wares['iron'] = wares['iron'] - number
    if(ichoice == "3"):
        if(wares['phone'] >= number):
            money = money + (prices['phone'] * number)
            wares['phone'] = wares['phone'] - number
    
def buyGoods():
    '''
    A function that lets the player buy goods from the planet and subtracts the
    money from his total amount of money
    '''
    #variables
    global wares
    global money
    prices = activePlanet.getPrices()
    #function
    print("The prices are as followed")
    for key,value in prices.items():
        print(key +": " + str(value))
    ichoice = input("What do you want to buy: wheat[1], iron[2] or phones[3]?")
    number = int(input("How many do you want to buy?"))
    if(number >= cargoSpaceCalk()):
        if(ichoice == "1"):
            money = money - (prices['wheat'] * number)
            wares['wheat'] += number
        if(ichoice == "2"):
            money = money - (prices['iron'] * number)
            wares['iron'] += number
        if(ichoice == "3"):
            money = money - (prices['phone'] * number)
            wares['phone'] += number
    else:
        print("Not enough Space")
    input("Press return to continue")
    
        

def chooseDest():
    '''
    A function that creates a planet from the users choice and returns that 
    planet.
    '''
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
           
def buyShip():
    '''
    A function that allows the player to buy ships
    '''
    #Variables
    global ships
    #function
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
        
def mainMenu():
    while(True):
        print("Welcome to " + activePlanet.__class__.__name__ + " planet " + activePlanet.getName())
        print("You have " + str(money) + " money")
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
            
        if(choice == "4"):
            buyGoods()
        if(choice == "5"):
            sellGoods()

#Setup
name = input("Please enter your name: ")
print("Welcome to SpaceSim " + name + "!")
print("Which planet would you like to travel to first? ")
activePlanet = chooseDest()
mainMenu()