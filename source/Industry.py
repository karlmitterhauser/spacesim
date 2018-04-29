'''
Created on 29 Apr 2018
This is the industry planet (inherits from Planet) 
iron prices are low, everything else has a high price
@author: Klaus
'''
from Planet import Planet
import random

class Industry(Planet):
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
        self.prices['wheat'] =  random.randint(35,50)
        self.prices['iron'] = random.randint(5,15)
        self.prices['phone'] = random.randint(35,50)
