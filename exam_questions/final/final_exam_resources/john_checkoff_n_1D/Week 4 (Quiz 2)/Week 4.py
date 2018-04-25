# -*- coding: utf-8 -*-
"""
Created on Sun Feb 11 18:36:43 2018

@author: jon_c
"""
import math
import numpy
import scipy

fruits = ["apple", "orange", "banana", "cherry"]
for afruit in fruits:     # by item
    print(afruit)

fruits = ["apple", "orange", "banana", "cherry"]
for position in range(len(fruits)):     # by index i don't get this one
    print(fruits[position])
    
    
for number in range(20):
    if number % 3 == 0:
        print(number)
        
numbers = [1, 2, 3, 4, 5]
print(numbers)

for i in range(len(numbers)):
    numbers[i] = numbers[i] ** 2

print(numbers)
alist = [4, 2, 8, 6, 5]
blist = [ ]
for item in alist:
    blist.append(item+5)
print(blist)


def doubleStuff(aList):
    """ Overwrite each element in aList with double its value. """
    for position in range(len(aList)):
        aList[position] = 2 * aList[position]

things = [2, 5, 9]
print(things)
doubleStuff(things)
print(things)



def doubleStuff(a_list):
    """ Return a new list in which contains doubles of the elements in a_list. """
    new_list = []
    for value in a_list:
        new_elem = 2 * value
        new_list.append(new_elem)
    return new_list

things = [2, 5, 9]
print(things)
things = doubleStuff(things)
print(things)


def primes_upto(n):
    """ Return a list of all prime numbers less than n. """
    result = []
    for i in range(2, n):
        if is_prime(i):
            result.append(i)
    return result

'''list comprehension, genereal syntax is: [<expression> for <item> in <sequence> if  <condition>]'''
mylist = [1,2,3,4,5]
yourlist = [item ** 2 for item in mylist]
print(yourlist)


alist = [4,2,8,6,5]
blist = [num*2 for num in alist if num%2==1]
print(blist)    


nested = ["hello", 2.0, 5, [10, 20]]
innerlist = nested[3]
print(innerlist)
item = innerlist[1]
print(item)
print(nested[3][1])


alist = [ [4, [True, False], 6, 8], [888, 999] ]    #wtf is this shit
if alist[0][1][0]:
   print(alist[1][0])
else:
   print(alist[1][1])

   
   
song = "The rain in Spain..."
wds = song.split()
print(wds)

song = "The rain in Spain..."
wds = song.split('ai')
print(wds)



wds = ["red", "blue", "green"]
glue = ';'
s = glue.join(wds)
print(s)
print(wds)
print("***".join(wds))
print("".join(wds))



myname = "Edgar Allan Poe"              'what is this shit too, pls explain'
namelist = myname.split()
init = ""
for aname in namelist:
    init = init + aname[0]
print(init)


#python in built function to create a list from whatever
xs = list("Crunchy Frog") 
print(xs)



julia = ("Julia", "Roberts", 1967, "Duplicity", 2009, "Actress", "Atlanta, Georgia")
print(julia[2])
print(julia[2:6])
print(len(julia))
julia = julia[:3] + ("Eat Pray Love", 2010) + julia[5:]
print(julia)



tup = (5,)
print(type(tup))
x = (5)
print(type(x))


def circleInfo(r):
    """ Return (circumference, area) of a circle of radius r """
    c = 2 * 3.14159 * r
    a = 3.14159 * r * r
    return (c, a)
print(circleInfo(10))



#dictionary

eng2sp = {}
eng2sp['one'] = 'uno'
eng2sp['two'] = 'dos'
eng2sp['three'] = 'tres'
print (eng2sp)

eng2sp = {'three': 'tres', 'one': 'uno', 'two': 'dos'}
print(eng2sp)
        
        
eng2sp = {'three': 'tres', 'one': 'uno', 'two': 'dos'}
value = eng2sp['two']
print(value)

inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}
del inventory['pears']
print(inventory)

inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}
inventory['pears'] = 0
print(inventory)

inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}
inventory['bananas'] = inventory['bananas'] + 200
numItems = len(inventory)
print(inventory['bananas'])

mydict = {"cat":12, "dog":6, "elephant":23}
mydict["mouse"] = mydict["cat"] + mydict["dog"]
print(mydict["mouse"])


inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}
for akey in inventory.keys():     # the order in which we get the keys is not defined
   print("Got key", akey, "which maps to value", inventory[akey])
ks = list(inventory.keys())
print(ks)


inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}
for k in inventory:
   print("Got key", k)


inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}
print(list(inventory.values()))
print(list(inventory.items()))
for (k,v) in inventory.items():
    print("Got", k, "that maps to", v)
for k in inventory:
    print("Got", k, "that maps to", inventory[k])


inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}
print('apples' in inventory)
print('cherries' in inventory)
if 'bananas' in inventory:
    print(inventory['bananas'])
else:
    print("We have no bananas")


inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}
print(inventory.get("apples"))
print(inventory.get("cherries"))
print(inventory.get("cherries", 0))

farm = {'cat':1, 'dog':2, 'chicken':3}
inputkey='dog'
for akey, value in farm.items():
    if akey == inputkey:
        print (farm[inputkey])































