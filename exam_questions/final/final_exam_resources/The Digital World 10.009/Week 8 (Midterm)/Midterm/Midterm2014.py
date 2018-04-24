# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 23:11:12 2018

@author: jon_c
"""

#question 1 
def stc(s1, s2):
    return(abs(len(s1)-len(s2)))

s1 = "SUTD"
s2 = "NUS"
print(stc(s1, s2))

s1 = "Japan"
s2 = "Singapore"
print(stc(s1, s2))

#%%
#question 2
def sumVal(d):
    if d == {}:
        return None
    else:
        key_lst = [key for key in d.keys() if key < 3]
        val_sum = 0
        for val in key_lst:
            val_sum += d.get(val)
    return val_sum

d = {4:-7, 8:4, 2:10, 1:-2}
print(sumVal(d))   


#%%
#question 3
def count(a,b,c):
    return(len(range(a,b)) > len(range(b,c)))

a=2
b=4
c=7
print(count(a,b,c))
a=3
b=7
c=-1
print(count(a,b,c))


#%%
#question 4























