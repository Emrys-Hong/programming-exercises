# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 00:24:49 2018

@author: jon_c
"""

#question 1
def compress(lst):
    lst1 = []
    lst2 = []
    lst3 = []
    
    tierone = 0
    tiertwo = 0
    tierthree = 0
    
    for tier1 in lst:
        tierone += tier1
        for tier2 in tier1:
            tiertwo +=tier2
        lst2.append(tiertwo)
    lst1.append(tierone)
    return lst1
    





print(compress([1,2,3]))
print(compress([1,2,[3,4]]))





















