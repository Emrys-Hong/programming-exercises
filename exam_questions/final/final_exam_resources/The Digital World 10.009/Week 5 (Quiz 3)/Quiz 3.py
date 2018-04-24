# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 12:02:23 2018

@author: jon_c
"""
inp = [[1,2,3],[2,6,3,8]]
def average_list(inp):
    avg_list=[]
    for x in inp:
        total = 0
        for y in x:
            total = total + y
            avg = int(total/len(x))
            
        avg_list.append(avg)
    return avg_list 
    
print(average_list(inp))