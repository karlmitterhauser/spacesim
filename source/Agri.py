'''
This is the agricultur planet (inherits from Planet) 
wheat prices are low, everything else has a high price
Created on 28 Apr 2018

@author: Klaus
'''
import Planet
import random

class Agri(Planet):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        super().__init__()
        self.setPrices()
    
    def getPrices(self):
        return self.prices 
    
    def setPrices(self):
        self.prices['wheat'] =  random.randint(5,15)
        self.prices['iron'] = random.randint(35,50)
        self.prices['phone'] = random.randint[35,50]
        
    def getName(self):
        return self.name