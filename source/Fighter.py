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
        self.firepower = self.price * 2

    def getFirepower(self):
        return self.firepower