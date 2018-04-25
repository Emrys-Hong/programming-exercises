# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 23:20:21 2018

@author: jon_c
"""

def linspace(start, stop, num=50):
  
    lst = [start]
    madadder = (stop - start) / (num -1)
    lst2 = start
    while lst2 < stop:
        lst2 += madadder
        lst.append(round(lst2,5))
    return lst