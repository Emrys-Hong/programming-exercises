# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 20:30:10 2018

@author: jon_c
"""

#question 1
import math
def combination(credit):
    credit = (credit - 10.0)/20.0
    out = 2.0*credit - 1.5
    return out
def activation(a):
    probability = 1.0/(1 + math.exp(-a))
    print (probability)
    #return probability ensures that output returns the probability instead of none.
credit = 16.0
output = activation( combination(credit) )
print (credit)
print (output)
#%%


#question 3
def area_r_polygon(n, s):
    area = (n * s**2)/ (4 * math.tan(math.pi / n))
    return round(area, 3)

print(area_r_polygon(5, 6.5))
print(area_r_polygon(7, 3.25))
print(area_r_polygon(2, 12.5))

#%%
#question 4
def mysum(a, b, limit):
    if type(a) is not int:
        return "Wrong input"
    elif type(b) is not int:
        return "Wrong input"
    elif a is 0:
        return "Wrong input"
    elif b is 0:
        return "Wrong input"
    else:
        summa = 0
        summb = 0
        lsta = []
        lstb = []
        
        for multipliera in range(limit):
            if a * multipliera < limit:
                lsta.append(a * multipliera)
            else:
                pass
            
        for multiplierb in range(limit):
            if b * multiplierb < limit:
                lstb.append(b * multiplierb)
            else:
                pass
        
        lst = list(set(lsta)|set(lstb))
        total = 0
        for i in lst:
            total += i
        return total
        
        
        
 
    
print (mysum(3, 5, 10))
print (mysum(2, 4, 12))
print (mysum(3, 3, 15))
print (mysum(7, 9, 100))
print (mysum(21, 34, 10000))
print (mysum (0, 5, 10))
print (mysum(0.5, 5, 10))
print (mysum(3, "x", 10))
print (mysum(2, 3, 0))

#they're overlapping rn, how to fix that
#%%
#question 5
def get_students(students, course):
    lst = []
    for i in range(len(students)):
        if course in students[i][1]: 
            lst.append(students[i][0])
    return lst
    
    
students = [("Alan", ["CompSci", "Physics", "Math"]), ("Justin", ["Math", "CompSci", "Stats"]),
            ("Edward", ["CompSci", "Philosophy", "Economics"]), ("Margaret", ["InfSys", "Accounting", "Economics", "CommLaw"]),
            ("Philip", ["Sociology", "Economics", "Law", "Stats", "Music"]), ("Mary", ["Math", "CompSci", "Stats"]),
            ("Vera", ["CompSci", "Philosophy", "Economics"]), ("Mike", ["InfSys", "Accounting", "Economics", "CommLaw"]),
            ("Donna", ["Sociology", "Economics", "Law", "Stats"])]

print (get_students(students, "Philosophy"))
print (get_students(students, "History"))
print (get_students(students, "Math"))
print (get_students(students, "CompSci"))


#%%
#question 6
#part a
def get_nodes(fid):
    lines = fid.readlines()    
    lines_s = [line.strip("\n") for line in lines]    
    lines_r = [line.strip("\r") for line in lines_s]    
    tuples_ = [line.split(" ") for line in lines_r]    
    tuples_i = [tuple([int(number) for number in pair]) for pair in tuples_]     
    return tuples_i 

#part b
def create_graph(nodes):
    
    
#part c
def get_friends(G, node):
    lst = []
    
    
#part d
def suggested_new_friends(G, node):
    

f = open('/Users/jon_c/Desktop/The Digital World 10.009/Week 8 (Midterm)/Midterm/text_files/midterm2017/facebook_less.txt','r') #Change accordingly
nodes= get_nodes(f)
G = create_graph(nodes)
print ('Friends of 1 from facebook_less.txt')
print (get_friends(G,1))
print ('Suggested new friends for 1')
print (suggested_new_friends(G,1))
f.close()

f = open('/Users/jon_c/Desktop/The Digital World 10.009/Week 8 (Midterm)/Midterm/text_files/midterm2017/sutdbook1.txt','r') #Change accordingly
nodes= get_nodes(f)
G = create_graph(nodes)
print ('Friends of 0 from sutdbook1.txt')
print (get_friends(G,0))
print ('Suggested new friends for 0')
print (suggested_new_friends(G,0))
f.close()

f = open('/Users/jon_c/Desktop/The Digital World 10.009/Week 8 (Midterm)/Midterm/text_files/midterm2017/sutdbook2.txt','r') #Change accordingly
nodes= get_nodes(f)
G = create_graph(nodes)
print ('Friends of 0 from sutdbook2.txt')
print (get_friends(G,0))
print ('Suggested new friends for 0')
print (suggested_new_friends(G,0))
f.close()





#%%
#question 7























































