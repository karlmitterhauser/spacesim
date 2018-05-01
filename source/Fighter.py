'''
Created on 01.05.2018

@author: Karl
'''
from Spaceship import Spaceship
from random import randint

'''
SubClass of the Spaceship class which defines the Fighter - Spaceship
It introduces the new fields firepower and type

firepower: how much damage the ship can deal in combat
type: What kind of ship it is
'''

class Fighter(Spaceship):
    def __init__(self):
        super().__init__()
        self.firepower = randint(100, 150)
        self.type = "Fighter"
        
    def getFirepower(self):
        return self.firepower
    
    def getType(self):
        return self.type