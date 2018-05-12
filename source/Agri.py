'''
This is the agricultur planet (inherits from Planet) 
wheat prices are low, everything else has a high price
Created on 28 Apr 2018

@author: Klaus
'''
from Planet import Planet
import random

class Agri(Planet):
    '''
    This is a class that inherits from Planet, it inherits a name and a price
    dictionary
    '''

    def __init__(self):
        '''
        Constructor
        '''
        super().__init__()
        self.setPrices()
    
    def setPrices(self):
        self.prices['wheat'] =  random.randint(5,15)
        self.prices['iron'] = random.randint(35,50)
        self.prices['phone'] = random.randint(35,50)
        