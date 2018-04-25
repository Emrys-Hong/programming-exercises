# -*- coding: utf-8 -*-
"""
Created on Sun Feb 18 21:49:52 2018

@author: jon_c
"""

import random

prob = random.random()
print(prob)

diceThrow = random.randrange(1, 7)       # return an int, one of 1,2,3,4,5,6
print(diceThrow)


prob = random.random()
result = prob * 5
print(result)





def square(x):
    runningtotal = 0
    for counter in range(x):
        
        runningtotal = runningtotal + x

    return runningtotal

toSquare = 10
squareResult = square(toSquare)
print("The result of", toSquare, "squared is", squareResult)



def square(x):
     y = x * x
     return y

def sum_of_squares(x, y, z):
    a = square(x)
    b = square(y)
    c = square(z)
    return a + b +c

a = -5
b = 2
c = 10
result = sum_of_squares(a, b, c)
print(result)