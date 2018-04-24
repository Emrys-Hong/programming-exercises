# -*- coding: utf-8 -*-
"""
Created on Mon Apr 23 23:34:46 2018

@author: jon_c
"""

#question 1
import math
class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __str__(self):
        return ("Point2D(" + str(self.x) + "," + str(self.y) + ")")
        
    def add(self, x, y):
        return (self.x + x, self.y + y)
        
    
class Vector2D:
    def __init__(self, dx, dy):
        self.dx = dx
        self.dy = dy
        
    def length(self):
        return math.sqrt(self.dx**2 + self.dy**2)



p = Point2D(1,2)
v = Vector2D(3,1)
q = p.add(v)
print (q)

#%%
#question 2
from libdw import sm

class CombLock(sm.SM):
    start_state = "0"
    def getNextValues(self, state, inp):
        
        if (inp == 1):
            next_state = 1
            output = "locked"
            
        elif (state == 1 and inp == 2):
            next_state = 2
            output = "locked"
        
        elif (state == 2 and inp == 5):
            next_state = 5
            output = "locked"
        
        elif (state == 1 and inp == -1):
            next_state = -1
            output = "unlocked"
        
        else:   
            next_state = 0
            output = "unlocked"
            
        return next_state, output
            


lock = CombLock()

print (lock.transduce([1,2,5,-1]))

print (lock.transduce([1,0,2,5,-1]))

print (lock.transduce([3,2,5,-1]))

print (lock.transduce([1,2,5,-1,1,2,5,-1]))

print (lock.transduce([3,2,5,-1,1,2,5,-1])  )          
            
            
#%%          
import libdw.sm as sm
class CombLock(sm.SM):
    def __init__(self, keyList):
        self.keyList = keyList

    def getNextValues(self, state, inp):
        
        if inp == 0:
            next_state = "locked"
            output = "locked"

        elif inp >= 1 and inp <= 9:
            next_state = "locked"
            output = "locked"
            
            
        elif inp == -1:
            if 























