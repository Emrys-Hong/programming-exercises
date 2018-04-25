# -*- coding: utf-8 -*-
"""
Created on Sun Feb 18 21:46:17 2018

@author: jon_c
"""

#BOOLEANS
#x == y  Produce True if ... x is equal to y
#x != y  ... x is not equal to y
#x > y  ... x is greater than y
#x < y  ... x is less than y
#x >= y  ... x is greater than or equal to y
#x <= y  ... x is less than or equal to y

age = 18
old_enough_to_drive = age >= 17
print (old_enough_to_drive)

n = 6
test = n % 2 == 0 and n % 3 == 0 
print (test)

n = 6
test2 = n % 2 == 0 or n % 3 == 0 
print (test2)

#x and False == False
#False and x == False
#y and x == x and y
#x and True == x
#True and x == x
#x and x == x

#x or False == x
#False or x == x
#y or x == x or y
#x or True == True
#True or x == True
#x or x == x

#in and not in are boolean operators too
x = 10
y = 10

if x < y:
    print("x is less than y")
elif x > y:
    print("x is greater than y")
else:
    print("x and y must be equal")



def isDivisible(x, y):
    if x % y == 0:
        result = True
    else:
        result = False

    return result

if isDivisible(10, 5):
    print("That works")
else:
    print("Those values are no good")
    
def sumTo(aBound):
    theSum  = 0
    aNumber = 1
    while aNumber <= aBound:
        theSum = theSum + aNumber
        aNumber = aNumber + 1
    return theSum

print(sumTo(4))

print(sumTo(1000))

vocabulary = ["iteration", "selection", "control"]
numbers = [17, 123]
empty = []
mixedlist = ["hello", 2.0, 5*2, [10, 20]]

print(numbers)
print(mixedlist)
newlist = [ numbers, vocabulary ]
print(newlist)

alist =  ["hello", 2.0, 5, [10, 20]]
print(len(alist))
print(len(['spam!', 1, ['Brie', 'Roquefort', 'Pol le Veq'], [1, 2, 3]]))

numbers = [17, 123, 87, 34, 66, 8398, 44]
print(numbers[2])
print(numbers[9 - 8])
print(numbers[-2])
print(numbers[len(numbers) - 1])
#Remember that the indices start at 0

alist = [3, 67, "cat", [56, 57, "dog"], [ ], 3.14, False]
print(alist[2].upper())

alist = [3, 67, "cat", [56, 57, "dog"], [ ], 3.14, False]
print(alist[2][0])

fruit = ["apple", "orange", "banana", "cherry"]
print([1, 2] + [3, 4])
print(fruit + [6, 7, 8, 9])

print([0] * 4)
print([1, 2, ["hello", "goodbye"]] * 2)

a_list = ['a', 'b', 'c', 'd', 'e', 'f']
print(a_list[1:3])
print(a_list[:4])
print(a_list[3:])
print(a_list[:])

fruit = ["banana", "apple", "cherry"]
print(fruit)

fruit[0] = "pear"
fruit[-1] = "orange"
print(fruit)

alist = ['a', 'b', 'c', 'd', 'e', 'f']
alist[1:3] = ['x', 'y']
print(alist)

alist = ['a', 'b', 'c', 'd', 'e', 'f']
alist[1:3] = []
print(alist)

alist = ['a', 'b', 'c', 'd', 'e', 'f']
alist[1:3] = []
print(alist)

a = ['one', 'two', 'three']
del a[1]
print(a)

alist = ['a', 'b', 'c', 'd', 'e', 'f']
del alist[1:5]
print(alist)

a = [81, 82, 83]
b = [81, 82, 83]
print(a is b)
print(a == b)

alist = [4, 2, 8, 6, 5]
blist = alist
blist[3] = 999
print(alist)

a = [81, 82, 83]
b = a[:]       # make a clone using slice
print(a == b)
print(a is b)
b[0] = 5
print(a)
print(b)

origlist = [45, 76, 34, 55]
print(origlist * 3)
newlist = [origlist] * 3 #difference between this line and the one above
print(newlist)

origlist = [45, 76, 34, 55]
newlist = [origlist] * 3
print(newlist)
origlist[1] = 99
print(newlist)

alist = [4, 2, 8, 6, 5]
blist = [alist] * 2
alist[3] = 999
print(blist)


mylist = []
mylist.append(5)
mylist.append(27)
mylist.append(3)
mylist.append(12)
print(mylist)

mylist.insert(1, 12)
print(mylist)
print(mylist.count(12))

print(mylist.index(3))
print(mylist.count(5))

mylist.reverse()
print(mylist)

mylist.sort()
print(mylist)

mylist.remove(5)
print(mylist)

lastitem = mylist.pop()
print(lastitem)
print(mylist)


alist = [4, 2, 8, 6, 5]
alist.append(True)
alist.append(False)
print(alist)

alist = [4, 2, 8, 6, 5]
alist.insert(2, True)
alist.insert(0, False)
print(alist)

alist = [4, 2, 8, 6, 5]
temp = alist.pop(2)
temp = alist.pop()
print(alist)













   
    
    
    
    
    
    