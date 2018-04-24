# -*- coding: utf-8 -*-
"""
Created on Thu Mar  1 12:02:49 2018

@author: jon_c
"""
#%%
#gotta convert int to str

a = str(122344545)
print(type(a))
#%%

strnumber = str(number)

def is_valid(number):
    total = 0
    for eachchar in number[-2::-2]:
        total += eachchar
        return total
    
    partb = sum_of_double_even_place
    partc = sum_of_odd_place
    totalbc = partb + partc
    
    if totalbc % 10 == 0:
        return True
    else:
        return False
    
        

def get_digit(number):
    if len(number) == 1: #is one digit:
        return number
    else:
        #sum the digits
        total = 0
        for eachchar in number:
            total += eachchar
            return total
        

def sum_of_odd_place(number):
    total = 0
    for eachchar in number[-1::-2]:
        total += eachchar
        return total
        

def prefix_matched(number, d):
    if get_size == d:
        return True
    else:
        return False