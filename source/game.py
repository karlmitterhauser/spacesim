'''
Created on 29 Apr 2018
main game function at the moment it just tests if the name creation is correct
and if the prices are asssigned correctly for each planet type
@author: Klaus
'''
from Agri import Agri
from Industry import Industry
from HighTech import HighTech

if __name__ == '__main__':
    myPlanetA = Agri()
    print('Agriculture Planet = ' +myPlanetA.getName())
    pricel = myPlanetA.getPrices()
    for key,value in pricel.items():
        print('Price of ' +key+ ' is ' ,value)
        
    myPlanetB = Industry()
    print('Industry Planet = ' +myPlanetB.getName())
    pricel = myPlanetB.getPrices()
    for key,value in pricel.items():
        print('Price of ' +key+ ' is ' ,value)
        
    myPlanetC = HighTech()
    print('HighTech Planet = ' +myPlanetC.getName())
    pricel = myPlanetC.getPrices()
    for key,value in pricel.items():
        print('Price of ' +key+ ' is ' ,value)