# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 13:51:26 2018

@author: jon_c
"""
import math
#question 3
def comp(x):
    return (x**3 + 4 * x **2 + 6 * x + 1)

print (comp(2))


#%%
#question 4
def genList(n1,n2):
    lst = []
    for number in range(n1, n2 + 1):
        if number % 3 == 0:
            lst.append(number)
        else:
            continue
    return lst

print(genList(2, 12))
print(genList(2, 20))


#%%
#question 5
Z = []
def matAdd(A, B):
    for i in range(len(A)):
        row = []
        for j in range(len(A[i])):
            row.append(A[i][j] + B[i][j])
        Z.append(row)
        return Z

A = [[1,2,3], [4, 5, 6]]
B = [[10,20,30], [40, 50, 60]]
C = matAdd(A,B)
print ('A:', A, 'B:', B, 'C:', C)



#%%
#question 7
def countLitPixel(cx, cy, r):
    quadrant = 0
    for x in range(r+1):
        y = math.sqrt(r**2 - x**2)
        yprime = math.ceil(y)
        quadrant += yprime
        total = quadrant * 4
    return total
        

print(countLitPixel(5, 2, 5))
print(countLitPixel(1,1,1))
print(countLitPixel(0.02,0.578,5))  





















