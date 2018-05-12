'''
Created on 01.05.2018

@author: Karl
'''
from Spaceship import Spaceship
from random import randint

'''
SubClass of the Spaceship class which defines the Cargo - Spaceship
It introduces the new fields cargoDict, cargoSpace and type

cargoSpace: How many items the ship can store
cargoDict: Which items the ship stores in which quantity
type: What kind of ship it is
'''

class Cargo(Spaceship):
    def __init__(self):
        super().__init__()
        #self.cargoDict = {'wheat': 0, 'iron': 0, 'phone': 0}
        self.cargoSpace = randint(500, 1000)
        
    #def getCargoDict(self):
        #return self.cargoDict
    
    def getCargoSpace(self):
        return self.cargoDict