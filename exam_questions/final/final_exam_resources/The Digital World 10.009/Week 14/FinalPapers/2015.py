# -*- coding: utf-8 -*-
"""
Created on Sun Apr 22 23:12:17 2018

@author: jon_c
"""

#question 3

def Comptrace(A):
    lst = []
    m = 0
    for i in A:
#        print(A[m])
        for j in i:
#            print(i[m])
            lst.append(i[m])
            break 
        m += 1
    print(lst)
    summ = 0
    for a in lst:
        summ += a
    return summ

A = [[2.2, 2, 3.1], [4, 5, 6], [7, 8, 9]]
print(Comptrace(A))

#%%
#question 4

def findKey(dInput, strInput):
    keys = []
    for key, value in dInput.items():
        if value == strInput:
#            print (key)
            keys.append(key)
    sortlst = sorted(keys)   #sorted(a, reverse=True) for descending
    return sortlst

dInput = {1:'singapore', 20:'china', 4:'japan', 5:'china', 10:'japan'}
findKey(dInput, 'china')
print(findKey(dInput, 'china'))
findKey(dInput, 'korea')
print(findKey(dInput, 'korea'))

#%%
#question 5
class Square:
    def __init__(self, x = 0, y = 0 , sideLength = 1.0):
        self.x = x 
        self.y = y
        self.sideLength = sideLength
    
    def getCenter(self):
        return (self.x, self.y)
    
    def getSideLength(self):
        return (self.sideLength)
    
    def getArea(self):
        return (self.sideLength ** 2)
    
    def getPerimeter(self):
        return (self.sideLength * 4)
    
    def containPoint(self, px, py):
        bound = self.sideLength / 2
        
        if -bound + self.x <= px and px <= bound + self.x and -bound + self.y <= py and py <= bound + self.y:
            return True
        else:
            return False
    
    def containSquare(self, inSquare):
        
        
        
        
        
s = Square(x = 1, y = 1, sideLength = 2.0)

print (s.getCenter())

print (s.getSideLength())

print (s.getArea())

print (s.getPerimeter())

print (s.containPoint(0, 0))

print (s.containPoint(0, -0.5))

print (s.containPoint(1, 1.5))
#
#print (s.containSquare(Square(x = 1.5, y = 1, sideLength = 1)))
#
#print (s.containSquare(Square(x = 1.5, y = 1, sideLength = 1.1)))
#
s2 = Square()

print (s2.getCenter())

print (s2.getSideLength())

print (s2.getPerimeter())

#%%
#question 6
from libdw import sm

class Elevator(sm.SM):
    start_state = "1"
    def get_next_values(self,state,inp):
        
        if (state == "1" and inp == "Down" ):
            next_state = "1"
            output = "First"
            
        elif (state == "1" and inp == "Up"):
            next_state = "2"
            output = "Second"
            
        elif (state == "2" and inp == "Up"):
            next_state = "3"
            output = "Third"
            
        elif (state == "3" and inp == "Up"):
            next_state = "3"
            output = "Third"
            
        elif (state == "3" and inp == "Down"):
            next_state = "2"
            output = "Second"
            
        elif (state == "2" and inp == "Down"):
            next_state = "1"
            output = "First"
                       
        return next_state, output
 
e = Elevator()
print (e.transduce(['Up', 'Up', 'Up', 'Up', 'Down', 'Down', 'Down', 'Up']))



#%%
#question 7
def countNumOpenLocker(K):
    for i in K:
        













#%%




















