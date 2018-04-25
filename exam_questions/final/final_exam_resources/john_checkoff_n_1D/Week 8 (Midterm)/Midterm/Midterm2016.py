# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 22:34:43 2018

@author: jon_c
"""

#question 1

State the similarities and differences between list and dictionary data structures. 
State what kind of data is suitable for each data structure and give examples.
Similarities:
Both lists and dictionaries are mutable.
Both lists and dictionaries can be generated via comprehensions.
Both lists and dictionaries are part of the 'collections' module.
Both lists and dictionaries contain elements that can be of any combination of data types.
Differences:
Lists maintain order of their elements while dictionaries are unordered.
Lists allow duplication while dictionary items are unique.
List items are accessed by index while dictionary items are accessed by keys.
Lists are implemented internally as variable-length arrays while dictionaries are implemented internally as resizable hash tables.
Examples:
Use dictionaries to associate values with keys for efficient 'by key' seaching: 
Telephone { 'Drake' : '1-800-468-546325464' } 
Address { 'Sponge Bob' : '124 Conch Street, Bikini Bottom, Pacific Ocean' }
Translation { "EN" : "DE", "red" : "rot", "green" : "grün", "blue" : "blau", "yellow":"gelb" }
Use lists for an ordered sequence of items:
Race standings [ 'me', 'me', 'me again', 'you' ]
Instructions [ 'To add in pot:', 'shark', 'cuttlefish', 'squid', 'mantis shrimp', 'anemone' ]
Sensor readings [ '0.21532', '0.98765', '1.12353', '9999.99999' ]



#%%
#question 2






#%%
#question 3
def norm(z1,z2,z3):
    norm = abs((z1*z1.conjugate() +z2*z2.conjugate()+ z2*z2.conjugate())**.5)
    return round(norm, 3)

print ('test 1')
z1=1+3j
z2=-1+3j
z3=-1-3j
ans=norm(z1,z2,z3)
print (ans)
print ('test 2')
z1=1+2j
z2=-1+2j
z3=-1-2j
ans=norm(z1,z2,z3)
print (ans)
print ('test 3')
z1=1+1j
z2=-1+1j
z3=-1-1j
ans=norm(z1,z2,z3)
print (ans)
    
#%%
#question 4
def factors(n):
    lst = []
    #denominator = 1
    for denominator in range(1,n+1):
        if n % denominator == 0:
            lst.append(denominator)
            #denominator += 1
        else:
            continue
    return lst

print ('test 1')
ans=factors(6)
print (ans)
print ('test 2')
ans=factors(12)
print (ans)
print ('test 3')
ans=factors(7)
print (ans)
print ('test 4')
ans=factors(15)
print (ans)
print ('test 5')
ans=factors(21)
print (ans)
print ('test 6')
ans=factors(1)
print (ans)
print ('test 7')
ans=factors(9)
print (ans)


#%%
#question 5
def combinations(n1,n2):
    lst = []
    for i in range(n2 - n1 + 1):
        if i < n1:
            
            
    
            
    return (lst, len(lst))
            
            
        
    

    
#%%
#question 7
import math

def maxProductThree(num):
    lst = []
    for i in num:
        a = math.fabs(i)
        lst.append(a)
    lst.sort()
    print (lst)
    total = 1
    for j in range((len(lst) - 3), (len(lst))):
        total = total * lst[j]        
    return total
    #total = lst[-1] * lst[-2] * lst[-3]
    #return total
            

import time
start_time = time.time()
num=[6,-3,-10,0,2]
print (maxProductThree(num))
num = [4, -139, -848, -142, -779, 406, 899, -932, 565, -678, -197, 442, 145, -711, -495, -743, 602, 841, 312, 104, 814, 771, 772, 292, -718, -151, 503, -265, -812, 792, 209, -734, -343, -674, 129, -421, -138, 826, -739, 625, 529, 391, 367, -166, 764, -178, -104, -380, -204, 697, -471, -811, -580, 207, -980, -983, -478, -551, -591, 121, -51, -424, 922, -521, -789, 30, -121, 847, 862, -232, -669, 990, -878, 690, 408, -452, -713, -644, -163, 526, -929, 767, -174, 110, 477, 188, 575, 328, 685, 93, 596, -865, -987, -321, 28, 383, -53, 405, 271, 783, 25, -255, -885, 747, -375, -44, -515, 598, 100, 830, 915, -663, -32, 112, -686, -796, 647, -397, -592, -309, -6, -706, -47, 116, 528, 454, -201, -303, -927, -418, -177, -858, -294, -449, 738, 573, -143, -331, 392, 958, -964, 742, -472, -650, 725, 555, 34, -130, -769, 835, -659, 849, 500, -850, 933, -70, -504, -729, 366, -224, -531, 780, -974, 83, -373, 273, -956, 187, 106, 549, -961, 509, 837, 72, -785, -871, 821, -915, 676, 185, 261, -558, 692, 37, -474, -641, -498, 949, 873, 494, 582, -698, 239, -153, 186, 167, -169, 198, -754, 409, 431, 437, -4, 147, 804, 157, 35, 332, -78, 18, -483, -487, -813, 160, -210, -493, 396, 280, 97, -445, -649, -306, 56, 965, 305, 231, -690, -681, 163, 325, -862, 492, 15, -903, -685, 558, -968, 307, 768, -112, 179, 267, 781, -268, 576, -429, 63, -828, 832, -798, -85, -56, 171, 11, -579, -897, 663, -337, 463, 518, 6, -437, 820, 33, 330, -280, 745, -179, -654, -79, -301, -106, -628, 840, 486, 643, 535, 664, 438, 612, -363, -757, -503, -857, -843, 143, -661, 831, 38, -444, -494, 656, 661, -906, -803, 991, -451, 336, 283, -243, 258, 40, -863, -920, -295, 372, -621, 128, 897, -762, 253, 774, -550, 445, -349, -118, 760, -642, 534, -683, -338, -252, 809, 574, -966, -208, -392, -889, 58, 174, -619, -446, 300, 952, 434, -538, 469, -809, -205, -780, 932, 653, -72, 715, 50, -367, 220, -501, 333, -296, 892, -788, 196, 749, 375, 240, 581, -516, -396, -901, -473, -967, 560, -870, -537, 217, 646, 483, 401, 282, 592, -833, 590, -340, 813, -583, 740, -186, -45, -390, 470, -251, 127, -202, 317, 137, 998, 793, -466, 569, 732, 381, 491, 140, -573, -786, 269, 517, -119, 674]
print (maxProductThree(num))
print("--- %s seconds ---" % (time.time() - start_time)) 


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    


























































