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
import sys
from random import randint
from random import uniform

#Variables
money = 1000
ships = []
wares = {'wheat' : 0, 'iron': 0, 'phone': 0}
name = None
activePlanet = None


#Methods
def randomEvent():
    '''
    A event that triggers randomly while traveling to the next planet. It 
    compares your firepower to the enemies firepower and whoever wins destroys 
    the fleet of the other player. (If you win you get some money)
    '''
    global money
    
    print("You are under attack Captain" +name)
    yourPower = firePowerCalk()
    print("Your firepower is " + str(firePowerCalk()))
    enemyPower = int(yourPower * round(uniform(0.9,1.1),1))
    print("The enemies firepower is " + str(enemyPower))
    if(enemyPower >= yourPower):
        print("You lose half your money")
        money = round(money/2)
    else:
        print("You win and get the money of the enemies(" +str(enemyPower)+")")
        money = money + enemyPower
    input("Press return to continue")   
     
def travel():
    '''
    A travel function that let's you decide on the planet you want to travel to.
    Sometimes it also triggers the randomEvent()
    '''
    chooseDest()
    if(randint(0,10) > 8):
        randomEvent()
    
def checkWares():
    '''
    A function that loops through the wares dictionary and displays the amount
    of wares the player has
    '''
    for key,value in wares.items():
        print(key +": " + str(value))

def firePowerCalk():
    '''
    Adds the Firepower of all the different fighter ships and returns the total
    value
    '''
    firepower = 0
    for s in ships:
        if(s.__class__.__name__ == "Fighter"):
            firepower += s.getFirepower()
    return firepower

def cargoSpaceCalk():
    '''
    Adds the CargoSpace of all the different cargoships and returns the total
    CargoSpace
    '''
    space = 0
    for s in ships:
        if(s.__class__.__name__ == "Cargo"):
            space += s.getCargoSpace()
    return space

def sellGoods(ichoice,number): 
    '''
    A function that sells the goods the player owns and adds the value of the 
    sold goods to the total amount of money.
    '''
    #variables
    global wares
    global money
    prices = activePlanet.getPrices()
    
    if(ichoice == 1):
        if(wares['wheat'] >= number):
            money = money + (prices['wheat'] * number)
            wares['wheat'] = wares['wheat'] - number
            print("You sold " +str(number)+ " wheat")
        else:
            print("Not enough wheat to sell")
    if(ichoice == 2):
        if(wares['iron'] >= number):
            money = money + (prices['iron'] * number)
            wares['iron'] = wares['iron'] - number
            print("You sold " +str(number)+ " iron")
        else:
            print("Not enough Iron to sell")
    if(ichoice == 3):
        if(wares['phone'] >= number):
            money = money + (prices['phone'] * number)
            wares['phone'] = wares['phone'] - number
            print("You sold " +str(number)+ " phones")
        else:
            print("Not enough phones to sell")


def buyGoods(ichoice,number):  
    global wares
    global money
    prices = activePlanet.getPrices()
    
    if(number <= cargoSpaceCalk()):
        if(ichoice == 1):
            checkmoney = money - (prices['wheat'] * number)
            if(checkmoney >= 0):
                money = money - (prices['wheat'] * number)
                wares['wheat'] += number
                print("You bought " +str(number)+ " wheat")
            else:
                print("Not enough money to buy this item")
        if(ichoice == 2):
            checkmoney = money - (prices['iron'] * number)
            if(checkmoney >= 0):
                money = money - (prices['iron'] * number)
                wares['iron'] += number
                print("You bought " +str(number)+ " iron")
            else:
                print("Not enough money to buy this item")
        if(ichoice == 3):
            checkmoney = money - (prices['phone'] * number)
            if(checkmoney >= 0):
                money = money - (prices['phone'] * number)
                wares['phone'] += number
                print("You bought " +str(number)+ " phones")
            else:
                print("Not enough money to buy this item")
    else:
        print("Not enough Space")

def marketplace():
    '''
    A function that lets the player buy goods from the planet and subtracts the
    money from his total amount of money
    '''
    #variables
    global wares
    global money
    prices = activePlanet.getPrices()
    #function
    print("The prices on the planet are as followed:")
    for key,value in prices.items():
        print(key +": " + str(value))
    print("You currently have the following resources:")
    for key,value in wares.items():
        print(key +": " + str(value))
    while (True):
        tchoice = input("Do you want to buy[buy], sell[sell] or exit[anything else]?")
        if(tchoice == "buy" or tchoice == "sell"):
            try:
                ichoice = int(input("What do you want to " +tchoice+ ": wheat[1], iron[2] or phones[3]?"))
                number = int(input("How many do you want to " +tchoice+ "?"))
            except:
                print("Please enter a valid number")
                print()
            if(0 < ichoice < 4):
                if(tchoice == "sell"):
                    sellGoods(ichoice,number)
                if(tchoice == "buy"):
                    buyGoods(ichoice,number)
            else:
                print("Please enter a valid number")  
        else:
            break
     
def chooseDest():
    '''
    A function that creates a planet from the users choice
    '''
    #Variables
    global activePlanet
    #function
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
           
def buyShip():
    '''
    A function that allows the player to buy ships
    '''
    #Variables
    global ships
    global money
    #function
    while True:
        print("Current money: " + str(money))
        print("What would you like to buy?")
        print("[1] Fighter Ship")
        print("[2] Cargo Ship")
        print("[0] Nothing")
        choice = input()
        if(choice == '1'):
            tempShip = Fighter()
            print("Price: " + str(tempShip.getPrice()))
            print("Firepower: " + str(tempShip.getFirepower()))
            print()
            print("[1] Confirm purchase")
            print("[2] Go back to overview")
            print("[3] Leave shop")
            pchoice = input()
            if pchoice == '1':
                if money >= tempShip.getPrice():
                    money = money - tempShip.getPrice()
                    ships.append(tempShip)
                    print("You bought a Fighter Ship")
                    print()
                    break
                else:
                    print("You can't afford this ship")
                    print()
            if pchoice == '3':
                break
            
        if(choice == '2'):
            tempShip = Cargo()
            print("Price: " + str(tempShip.getPrice()))
            print("Cargo Space: " + str(tempShip.getCargoSpace()))
            print()
            print("[1] Confirm purchase")
            print("[2] Go back to overview")
            print("[3] Leave shop")
            pchoice = input()
            print()
            if pchoice == '1':
                if money >= tempShip.getPrice():
                    money = money - tempShip.getPrice()
                    ships.append(tempShip)
                    print("You bought a Cargo Ship")
                    print()
                    break
                else:
                    print("You can't afford this ship")
                    print()
            if pchoice == '3':
                break        
        if(choice == '3'):
            break       
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
    input("Press return to continue")
        
def mainMenu():
    while(True):
        print ("\n" * 100)
        print("---------------------------------------------------------------")
        print("Welcome to " + activePlanet.__class__.__name__ + " planet " + activePlanet.getName())
        print("You have " + str(money) + " money")
        print("Your current free Cargospace is: " +str(cargoSpaceCalk() - wares['wheat'] - wares['iron'] - wares['phone']))
        print("Your current Firepower is: " +str(firePowerCalk()))
        print("")
        print("What would you like to do?")
        print("[1] Buy ships")
        print("[2] Go to the marketplace")
        print("[3] Travel to the next planet")
        print("[0] Exit Game")
        choice = 0
        choice = input()
        if(choice == "1"):
            buyShip()   
        elif(choice == "2"):
            marketplace()
        elif(choice == "3"):
            travel()
        elif(choice == "0"):
            print("See you later Captain")
            sys.exit(0)
        else:
            print("Wrong Input")
#Setup
name = input("Please enter your name: ")
print("Welcome to SpaceSim " + name + "!")
print("Which planet would you like to travel to first? ")
chooseDest()
mainMenu()
