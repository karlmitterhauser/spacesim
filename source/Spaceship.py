'''
Created on 28.04.2018

@author: Karl
'''
from random import randint
from abc import ABC, abstractmethod
'''
Class that defines the basic traits all Spaceships have in common
(price, hitpoints)

price: Defines the price of the ship
hitpoint: How much damage a ship can take before it breaks
'''

class Spaceship(ABC):
    def __init__(self):
        self.price = randint(80, 120)
        self.hitpoints = randint(100, 200)
     
    def getPrice(self):
        return self.price
    
    def getHitpoints(self):
        return self.hitpoints