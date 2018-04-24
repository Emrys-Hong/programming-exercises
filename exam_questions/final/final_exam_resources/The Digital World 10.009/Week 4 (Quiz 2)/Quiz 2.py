# -*- coding: utf-8 -*-
"""
Created on Thu Feb 15 14:53:37 2018

@author: jon_c
"""

def printvals(n):
    #newlist = []
    #newlist.append(n)
    intervalist = []
    i = 1
    while i <= n:
        if i % 5 == 0 and i % 7 == 0:
            #newlist[n] = 'A'
            intervalist.append('AB')
            #i += 1
        elif i % 7 == 0:
            #newlist[n] = 'B'
            intervalist.append('B')
            #i += 1
        elif i % 5 == 0:
            #newlist[n] = 'AB'
            intervalist.append('A')
            #i += 1
        else:
            intervalist.append(i)
        i += 1
    return intervalist
        
        
print(printvals(35))

