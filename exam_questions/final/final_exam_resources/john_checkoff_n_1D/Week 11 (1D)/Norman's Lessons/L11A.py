#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 31 17:37:56 2018

@author: norman_lee
"""

import math 

'''
this is your class definition
''' 
class Coordinate:
    
    def __init__(self,x = 0,y = 0):
        self.x = x
        self.y = y 
        
    def magnitude(self):
        return math.sqrt(self.x**2 + self.y**2)
    
    def __str__(self):
        return '(' + str(self.x) + ',' + str(self.y) +')'

'''You want this code to be executed 
when this file is run directly'''
def main():
    c= Coordinate(3,2)
    print(c)

'''therefore the python special variable
__name__ is set to this '''
print('__main__ in L11A',__name__)
if __name__=='__main__':
    print('L11A is at top level')
    main()
else:
    print('L11A is imported')
