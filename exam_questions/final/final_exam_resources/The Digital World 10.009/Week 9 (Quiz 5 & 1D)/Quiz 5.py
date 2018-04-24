# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 12:19:44 2018

@author: jon_c
"""

class Triangle:
    
    def __init__(self, color = "green", filled = True, side1 = 1.0, side2 = 1.0, side3 = 1.0):
        self.color = color
        self.filled = filled
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        
    def perimeter(self):
        return (self.side1 + self.side2 + self.side3)
        