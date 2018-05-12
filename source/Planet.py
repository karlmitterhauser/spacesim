'''
This is a abstract planet class.
Created on 28 Apr 2018

@author: Klaus
'''
from abc import ABC, abstractmethod
import string
import random

class Planet(ABC):
    '''
    There are 3 types of planets agricultur, industry and hightech
    Depending on the planet types the wares have different prices
    '''

    def __init__(self):
        '''
        Constructor
        '''
        super().__init__()
        prices = {'wheat': 0, 'iron': 0, 'phone': 0}
        self.prices = prices
        self.name = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(6))
          
    def getPrices(self):
        return self.prices
    
    @abstractmethod
    def setPrices(self):
        pass
    
    def getName(self):
        return self.name 