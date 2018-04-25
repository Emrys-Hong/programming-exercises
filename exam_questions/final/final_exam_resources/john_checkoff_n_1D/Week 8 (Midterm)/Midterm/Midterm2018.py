# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 14:35:42 2018

@author: jon_c
"""



my_string = "Computing"  
for character in my_string:
    print(character)
    if character == "u":
        print("Found 'u' :)")   
        break
        
    
    
    
    
    
#%%
def my_function(n): 
    #return_value = None 
    #if n == 0 or n == 1: 
     #   return_value = False 
    i=2 
    while i < n**0.5: 
        if n%i==0: 
            return_value = False 
            break 
        i+=1 
        return_value = True 
    return return_value

print(my_function(37))

#%%
import math

def area_square(s):
    return (s**2)

def vol_frustum(top_area, bottom_area, height):
    return ((height/3)*(top_area + bottom_area + math.sqrt(top_area * bottom_area)))
    

def get_volume(s1, s2, height):
    bottomarea = area_square(s1)
    toparea = area_square(s2)
    totalvol = vol_frustum(toparea,bottomarea, height)
    return round(totalvol, 3)


#%%
def determinant(matrix):
    if len(matrix) != len(matrix[0]):
        return None
    elif len(matrix) == 1:
        return (matrix[0][0])
    elif len(matrix) == 2:
        return ((matrix[0][0] * matrix [1][1]) - (matrix[0][1] * matrix[1][0]))
    elif len(matrix) == 3:
        return ((matrix[0][0] * ((matrix[1][1] * matrix[2][2]) - (matrix[1][2] * matrix[2][2]))) - (matrix[0][1] * ((matrix[1][0] * matrix[2][2]) - (matrix[1][2] * matrix[2][0]))) 
    + (matrix[0][2] * ((matrix[1][0] * matrix[2][1]) - (matrix[1][1] * matrix[2][0]))))

print(determinant([[23], [-4, 4]]))
print(determinant([[-5, -4], [-2, -3]])
print(determinant([[2, -3, 1], [2, 0, -1], [1, 4, 5]]))

#%%
matrix = [[23], [-4, 4]]
#print (matrix[0] * matrix[0][0])
a = matrix[0]
print (matrix[0][0])
#%%

matrix = [[-5, -4], [-2, -3]]
print (matrix[0][0])
#%%

matrix = [[2, -3, 1], [2, 0, -1], [1, 4, 5]]
print (matrix[0][0])

#%%
def nroot(n,i,num):
    fx = x ** n - num
    fprime = (n * x ** (n-1) 
    for a in range(i):
        iterative = i - (fx / fprime)
    return iterative



    #%%
    
def test(n, i, num):
    for x in range(i):
        return("shit")
    
print(test(2,10,2))
    
    
    
    
    
    
    
    
    
    
    

