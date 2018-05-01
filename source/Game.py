'''
Created on 01.05.2018

@author: Karl
'''
from Fighter import Fighter
from Cargo import Cargo

money = 1000
ships = []
name = None

#Player introduction
name = input("Please enter your name: ")
print("Welcome to SpaceSim" + name + "!")

#Giving the player the opportunity to purchase a ship
choice = int(input("Would you like to buy a Fighter[1] or a cargo ship[2] or nothing[3]? "))
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