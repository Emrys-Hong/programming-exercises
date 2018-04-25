# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 15:43:18 2018

@author: jon_c
"""

fruit = "banana"
bakedGood = " nut bread"
print(fruit + bakedGood)


fruit = "banana"
bakedGood = "nut bread"
print(fruit + bakedGood)


print("Go" * 6)
name = "Packers"
print(name * 3)
print(name + "Go" * 3)
print((name + "Go") * 3)


school = "Luther College"
m = school[2]
print(m)
lastchar = school[-1]
print(lastchar)


ss = "Hello, World"
check = "l"
new = "p"
print(ss.upper())
tt = ss.lower()
print(tt)
print(ss.count(check))
print(ss.replace(check,new))
print(ss.find(check, 5))
print(ss.split())


tobelist = "abcdefg"
print(" ".join(tobelist))
lst = tobelist.split()
print(lst)


acceptable = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
strspace = (" ".join(acceptable))
lst = strspace.split()
print(lst)
    

s = "python rocks"
print(s[1] * s.index("n"))


ss = "    Hello, World    "
els = ss.count("l")
print(els)
print("***" + ss.strip() + "***")
print("***" + ss.lstrip() + "***")
print("***" + ss.rstrip() + "***")
news = ss.replace("o", "***")
print(news)


food = "banana bread"
print(food.capitalize())
print("*" + food.center(25) + "*")
print("*" + food.ljust(25) + "*")     # stars added to show bounds
print("*" + food.rjust(25) + "*")
print(food.find("e"))
print(food.find("na"))
print(food.find("b"))
print(food.rfind("e"))
print(food.rfind("na"))
print(food.rfind("b"))
print(food.index("e"))


fruit = "Banana"
print(len(fruit))
print(len("Banana"))


fruit = "Banana"
sz = len(fruit)
last = fruit[sz - 1]     
print(last)
lastcharacter = fruit[len(fruit)-1]
print(lastcharacter)


singers = "Peter, Paul, and Mary"
print(singers[0:5])
print(singers[7:11])
print(singers[17:21])


fruit = "banana"
print(fruit[:3])
print(fruit[3:])
print(fruit[0:5:2])

word = "banana"
if word == "banana":
    print("Yes, we have bananas!")
else:
    print("Yes, we have NO bananas!")
    
    
word = "zebra"
if word < "banana":
    print("Your word, " + word + ", comes before banana.")
elif word > "banana":
    print("Your word, " + word + ", comes after banana.")
else:
    print("Yes, we have no bananas!")


print("apple" < "banana")
print("apple" == "Apple")
print("apple" < "Apple")
print("Apple" < "apple")


print(ord("A"))
print(ord("B"))
print(ord("5"))
print(ord("a"))
print("apple" > "Apple")

print(chr(65))
print(chr(66))
print(chr(49))
print(chr(53))
print("The character for 32 is", chr(32), "!!!")
print(ord(" "))


#Strings are immutable, which means you cannot change an existing string. 
#The best you can do is create a new string that is a variation on the original.


greeting = "Hello, world!"
newGreeting = 'J' + greeting[1:]
print(newGreeting)
print(greeting)       
new = greeting.replace("H", "h")
print(new)
test = greeting.replace("l", "LOL", 5)
print(test)


for aname in ["Joe", "Amy", "Brad", "Angelina", "Zuki", "Thandi", "Paris"]:
    invitation = "Hi " + aname + ".  Please come to my party on Saturday!"
    print(invitation)
    
for avalue in range(10):
    print(avalue)
    
    
for achar in "Go Spot Go":
    print(achar, 2, achar)
    
s = "python rocks"
for ch in s:
    print("HELLO")

s = "python rocks"
for ch in s[3:8]:
    print("HELLO")
    
    
fruit = "apple"
for idx in range(5):
    currentChar = fruit[idx]
    print(currentChar)

fruit = "apple" 
for idx in range(len(fruit)):
    print(fruit[idx])


fruit = "apple"   #apple in reverse
for idx in range(len(fruit)-1, -1, -1):
    print(fruit[idx])


s = "python rocks"
for idx in range(len(s)):
    if idx % 2 == 0:
        print(s[idx])


fruit = "apple"
position = 0
while position < len(fruit):
    print(fruit[position])
    position = position + 1
    

s = "python rocks"
idx = 1
while idx < len(s):
    print(s[idx])
    idx = idx + 2
    
    
print('p' in 'apple')
print('i' in 'apple')
print('ap' in 'apple')
print('pa' in 'apple')
print('a' in 'a')
print('apple' in 'apple')
print('' in 'a')
print('' in 'apple')
print('x' not in 'apple')


def removeVowels(s):
    vowels = "aeiouAEIOU"
    sWithoutVowels = ""
    for eachChar in s:
        if eachChar not in vowels:
            sWithoutVowels = sWithoutVowels + eachChar
    return sWithoutVowels
print(removeVowels("compsci"))
print(removeVowels("aAbEefIijOopUus"))

def removeletters(s):
    spaces = "\n\t"
    final = ""
    for eachspace in s:
        if eachspace not in spaces:
            final += eachspace
    return final
print(removeVowels("compsci"))
print(removeVowels("aAbEefIijOopUus"))



def count(text, aChar):
    lettercount = 0
    for c in text:
        if c == aChar:
            lettercount = lettercount + 1
    return lettercount
print(count("banana","a"))


def find(astring, achar):
    """
    Find and return the index of achar in astring.
    Return -1 if achar does not occur in astring.
    """
    ix = 0
    found = False
    while ix < len(astring) and not found:
        if astring[ix] == achar:
            found = True
        else:
            ix = ix + 1
    if found:
        return ix
    else:
        return -1
print(find("Compsci", "p"))
print(find("Compsci", "C"))
print(find("Compsci", "i"))
print(find("Compsci", "x"))


def find2(astring, achar, start):
    """
    Find and return the index of achar in astring.
    Return -1 if achar does not occur in astring.
    """
    ix = start
    found = False
    while ix < len(astring) and not found:
        if astring[ix] == achar:
            found = True
        else:
            ix = ix + 1
    if found:
        return ix
    else:
        return -1
print(find2('banana', 'a', 2))


def find3(astring, achar, start=0):
    """
    Find and return the index of achar in astring.
    Return -1 if achar does not occur in astring.
    """
    ix = start
    found = False
    while ix < len(astring) and not found:
        if astring[ix] == achar:
            found = True
        else:
            ix = ix + 1
    if found:
        return ix
    else:
        return -1
print(find3('banana', 'a', 2))


def find4(astring, achar, start=0, end=None):
    """
    Find and return the index of achar in astring.
    Return -1 if achar does not occur in astring.
    """
    ix = start
    if end == None:
        end = len(astring)

    found = False
    while ix < end and not found:
        if astring[ix] == achar:
            found = True
        else:
            ix = ix + 1
    if found:
        return ix
    else:
        return -1

ss = "Python strings have some interesting methods."
print(find4(ss, 's'))
print(find4(ss, 's', 7))
print(find4(ss, 's', 8))
print(find4(ss, 's', 8, 13))
print(find4(ss, '.'))


#%%
qbfile = open("qbdata.txt", "r")

for aline in qbfile:
    values = aline.split()
    print('QB ', values[0], values[1], 'had a rating of ', values[10] )

qbfile.close()




infile = open("qbdata.txt", "r")
>>> aline = infile.readline()
>>> aline
'Colt McCoy QB, CLE\t135\t222\t1576\t6\t9\t60.8%\t74.5\n'
>>>
>>> infile = open("qbdata.txt", "r")
>>> linelist = infile.readlines()
>>> print(len(linelist))
34
>>> print(linelist[0:4])
['Colt McCoy QB CLE\t135\t222\t1576\t6\t9\t60.8%\t74.5\n',
 'Josh Freeman QB TB\t291\t474\t3451\t25\t6\t61.4%\t95.9\n',
 'Michael Vick QB PHI\t233\t372\t3018\t21\t6\t62.6%\t100.2\n',
 'Matt Schaub QB HOU\t365\t574\t4370\t24\t12\t63.6%\t92.0\n']
>>>
>>> infile = open("qbdata.txt", "r")
>>> filestring = infile.read()
>>> print(len(filestring))
1708
>>> print(filestring[:256])
Colt McCoy QB CLE   135     222     1576    6       9       60.8%   74.5
Josh Freeman QB TB  291     474     3451    25      6       61.4%   95.9
Michael Vick QB PHI 233     372     3018    21      6       62.6%   100.2
Matt Schaub QB HOU  365     574     4370    24      12      63.6%   92.0
Philip Rivers QB SD 357     541     4710    30      13      66.0%   101.8
Matt Ha




infile = open("qbdata.txt", "r")
line = infile.readline()
while line:
    values = line.split()
    print('QB ', values[0], values[1], 'had a rating of ', values[10] )
    line = infile.readline()

infile.close()





















