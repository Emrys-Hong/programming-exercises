# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 15:43:31 2018

@author: jon_c
"""

#question 1
def reverse(string):
    return(string[-2::-2])
    
string = "testing"
print(reverse(string))
#%%

#question 1 alternative
def reverse(string):
    rev = ""
    for eachchar in range(len(string), 0, -1):
        rev += string[eachchar-1]
    return rev
        
print(reverse("testing"))

#%%

#question 2
def check_password(password):
    acceptable = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    notallowed = "!@#$%^&*()"
    if len(password) >= 8:
        for eachchar in password:
            if eachchar in notallowed:
                return False
        for eachchar in password:    
            if eachchar in acceptable:
                counter = 0
                for eachchar in password:
                    if eachchar in "1234567890":
                        counter += 1
                    else:
                        continue 
                if counter >= 2:
                    return True
                else:
                    return False
            else:
                return False
    else:
        return False
print(check_password("testest22***"))

#%%
#question 3
def longest_common_prefix(string1, string2):
    answer = ""
    len1, len2 = len(string1), len(string2)
    for i in range(len1):
        match = ""
        for j in range(len2):
            if (i + j < len1 and string1[i + j] == string2[j]):
                match += string2[j]
            else:
                if (len(match) > len(answer)): answer = match
                match = ""
    return answer


#%%
#question 4
from math import sqrt

class Coordinate:
    x = 0
    y = 0

def get_maxmin_mag(f):
    
    filestuff = f.read().split()
    highcoordinate = Coordinate()   
    lowcoordinate = Coordinate()
    
    highcoordinate.x = float(filestuff[0])
    highcoordinate.y = float(filestuff[1])
    highmag = sqrt((highcoordinate.x)**2 + (highcoordinate.y)**2)
    
    lowcoordinate.x = float(filestuff[0])
    lowcoordinate.y = float(filestuff[1])
    lowmag = sqrt((lowcoordinate.x)**2 + (lowcoordinate.y)**2)
    
    for index in range(2, len(filestuff), 2): 
        new_mag = sqrt((float(filestuff[index]))**2 + (float(filestuff[index + 1]))**2)
        if new_mag > highmag: 
            highmag = new_mag
            highcoordinate.x = float(filestuff[index])
            highcoordinate.y = float(filestuff[index + 1])
        elif new_mag < lowmag: 
            lowmag = new_mag
            lowcoordinate.x = float(filestuff[index])
            lowcoordinate.y = float(filestuff[index + 1])
    return (highcoordinate, lowcoordinate)


print(get_maxmin_mag(f))


#%%
#hw question 1
def binary_to_decimal(binstr):
    result = 0
    for bit in binstr:
        result = result * 2
        if bit == '1':
            result +=1
    return result


#%%
#hw question 2
def uncompressed1(string):
    i = 0
    newstring = ""
    number = 1
    while i <len(string):
        if string[i].isdigit():
            number = int(string[i])
        else:
            character = string[i]
            newstring += character * number
            number = 1
        i += 1
    return newstring
    
        
    
#%%
#hw question 3
def get_base_counts(DNA):
    lst = list(DNA)
    a_count = 0
    c_count = 0
    t_count = 0
    g_count = 0
    for i in lst:
        if i == "A":
            a_count += 1
        elif i == "C":
            c_count += 1
        elif i == "T":
            t_count += 1
        elif i == "G":
            g_count += 1
    finalthing = { "A" : a_count, "C" : c_count, "G" : g_count, "T": t_count}
    return finalthing


def get_base_counts2(dna):
    for i in dna:
        if i.islower() is True or i.isdigit() is True:
            return 'The input DNA string is invalid'    
    else:
        return get_base_counts(dna)

print(get_base_counts2('CCCCCGAAAAAAGGGTDDDDTT'))

#%%
#hw question 4
f = open('constants.txt','r')
def get_fundamental_constants(f):
    file = f.read().split('\n') # splits the file into multiple lines
    ans = {} #answer dictionary
    for i in range(2,len(file)-1): #goes from 2nd line to last line
        linevalues = file[i].split() #splits the line into it's individual elements
        ans[linevalues[0]] = float(linevalues[1]) #appending the key value pair
    return ans

print(get_fundamental_constants(f))


#%%
#hw question 5
f = open('scores.txt','r')
def process_scores(f):
    scores = f.read()
    morescores = scores.split()
    total = 0
    count = 0
    for each in morescores:
        total += float(each)
        count += 1
    average = total / count
    return (total, average)

print(process_scores(f))



























