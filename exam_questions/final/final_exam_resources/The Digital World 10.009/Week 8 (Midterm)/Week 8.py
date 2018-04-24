# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 12:37:08 2018

@author: jon_c
"""
import math
class Point:
    """ Point class for representing and manipulating x,y coordinates. """

    def __init__(self, initX, initY):
        """ Create a new point at the given coordinates. """
        self.x = initX
        self.y = initY

    def getX(self):
        return self.x * 2

    def getY(self):
        return self.y * 2
    
    def distanceFromOrigin(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5
    
    def __str__(self):
        return "x=" + str(self.x) + ", y=" + str(self.y)
    
    def halfway(self, target):
         mx = (self.x + target.x) / 2
         my = (self.y + target.y) / 2
         return Point(mx, my)

def distance(point1, point2):
    xdiff = point2.getX() - point1.getX()
    ydiff = point2.getY() - point1.getY()

    dist = math.sqrt(xdiff**2 + ydiff**2)
    return dist

p = Point(4, 3)
q = Point(5, 12)
mid = p.halfway(q)

print(mid)
print(mid.getX())
print(mid.getY())
print(p)
print(distance(p, q))
print(p.getX())
print(p.getY())
print(p.distanceFromOrigin())
#%%





















