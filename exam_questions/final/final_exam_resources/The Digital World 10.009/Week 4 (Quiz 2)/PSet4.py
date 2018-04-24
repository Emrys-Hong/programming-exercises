# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 11:51:27 2018

@author: jon_c
"""
#question 1

x=[1 ,2 ,3]
x[0]=0
y=x
y[0]= 1
print(x[0])
#%%
x=[1 ,2 ,3]
def f(l):
    l[0]= 'a'
f(x)
print(x[0])

x=[1 ,2 ,3]
y=[x]
a=[y,x]
y [0][0] = (1 ,2)
print (a[0][0][0][0])

x=[1 ,2 ,3]
y1 =[x ,0]
y2=y1 [:]
y2 [0][0]=0
y2 [1]=1
print (y1 [0][0])
print (y1 [1]) 
print (y2 [0][0]) 
print (y2 [1])

import copy
x=[1 ,2 ,3]
y1 =[x ,0]
y2= copy . deepcopy (y1)
y2 [0][0]=0
y2 [1]=1
print (y1 [0][0]) # (a)
print (y1 [1]) # (b)
print (y2 [0][0]) # (c)
print (y2 [1]) # (d)

l=[1 ,2 ,3]
#l [2:3]=4 # (a)
#print (l)
l [1:3]=[0] # (b)
print (l)
#l [1:1]=1 #(c)
#print (l)
l [2:]=[] # (d)
print (l)

#%%
#question 2
def compound_value_months(amt, rate, months):
    ans = 0
    for x in range(months):
        ans = (ans + amt) * (1 + rate/12)
    return round(ans, 2)


#%%
#question 3
lst=[[3,4],[5,6,7],[-1,2,8]]
def find_average(lst):
    sub_avg=[]
    new_lst=[]
    final=[]

    for x in lst:
        total = 0 
        for y in x:
            total += y
        if len(x) == 0:
            avg = 0.0
        else:
            avg = total / len(x)
        
        sub_avg.append(avg)

        bigsum = 0
        for y in x:
            new_lst.append(y)
        for i in range(len(new_lst)):
            bigsum += new_lst[i]
        totavg = bigsum / len(new_lst)

        final = sub_avg, totavg
    return sub_avg
    return final
    
print(find_average(lst))


#%%
#question 4

def transpose_matrix(lis):
    transposed = []
    if len(lis) == len(lis[0]):
        for i in range(len(lis)):
            t= []
            for j in range(len(lis[i])):
                t.append(lis[j][i])
            transposed.append(t)
    else:
        for i in range(len(lis[0])):
            t= []
            for j in range(len(lis)):
                t.append(lis[j][i])
            transposed.append(t)
    return transposed

print(transpose_matrix([[1,2],[3,4],[5,6]]))
print(transpose_matrix([[1,2,3],[4,5,6],[7,8,9]]))
'''
1 2
3 4
5 6

[[1,2,3],[4,5,6],[7,8,9]]     
1 2 3
4 5 6
7 8 9

[[1,4,7],[2,5,8],[3,6,9]]
1 4 7
2 5 8
3 6 9
'''

#%%
#hw question 1
def f_to_c(f):
    c = (f-32)*(5/9)
    return round(c, 1)

def f_to_c_approx(f):
    c_approx = (f-30)/2
    return round(c_approx, 1)


def get_conversion_table_a():
    conversion_table = [[x, f_to_c(x), f_to_c_approx(x)] for x in range(0, 110, 10)]
    return conversion_table
 
def get_conversion_table_b():
    x_list = [x for x in range(0, 110, 10)]
    c_list = [f_to_c(x) for x in range(0, 110, 10)]
    approx_x_list = [f_to_c_approx(x) for x in range(0, 110, 10)]
    return [x_list, c_list, approx_x_list]

#%%
#hw question 2
inlist = [[100, 20, 240],[1,7],[-8,-2,-1],[2]]

import sys

def max_list(inlist):
    list_max = []
    for a_list in inlist:
        maximum = -999999999
        n = 0
        for number in a_list:
            maxi = a_list[0]
            if a_list[n] > maxi:
                a_list[n] = number
            if number > maximum:
                maximum = number         
            
        list_max.append(maximum)
        
    return (list_max)

print (max_list(inlist))


#%%
#hw question 2 alternative
inlist = [[100, 20, 500],[1,7],[-8,-2,-1],[2]]

import sys

def max_list(inlist):
    list_max = []
    for a_list in inlist:
        n = 0
        for highestnum in a_list:
            maxi = a_list[0]
            if a_list[n] > maxi:
                a_list[n] = highestnum
                
        list_max.append(highestnum)
        
    return (list_max)

print (max_list(inlist))


#%%
#hw question 3
def multiplication_table(n):
    if n < 1:
        return None
    else:
        bigtable = []
        for i in range(n):
            number = n * (i + 1)
            bigtable.append(number)
            
    return bigtable
print(multiplication_table(5))
#%%
#hw question 3 alternative
def multiplication_table(n):
    if n < 1:
        return None    
    else:
        table = []
        counter = 1
        for i in range(n):
            value = 0
            row_n = []
            while value < counter * n:
                value = value + (i + 1)   
                
                row_n.append(value)
                
            counter = counter + 1

            table.append(row_n)
    return (row_n)
print(multiplication_table(1010))


#%%
#hw question 3 alternative
def multiplication_table1(n):    
    datatable = []
    count = 1
    if n >= 1:        
        while count <= n:        
            subtable = []        
            subtable = list(range(1  *count, (n * count) + 1, count))                    
            datatable.append(subtable)        
            count += 1        
        return datatable    
    else:
        return None
print(multiplication_table(5))


#%%
#hw question 4
import sys

def most_frequent(lst):
    most_frequent_list = []
    dicta = {}

    for i in lst:  
        dicta[i] = dicta.get(i, 0) + 1
    
    number = 0
    for value in dicta.values():
        if value > number:
            number = value
        
    for (a,b) in dicta.items():
        if b == number:
            most_frequent_list.append(a)
    
    return(most_frequent_list)

print(most_frequent(lst))

#%%
#hw question 4 alternative

lst = [2,3,40,3,5,4,-3,3,3,2,0]

def most_frequent(lst):
    number_counter = {}
    for numbers in lst:
        if numbers in number_counter:
            number_counter[numbers] += 1
        else:
            number_counter[numbers] = 1

    common_numbers = sorted(number_counter, key = number_counter.get, reverse = True)
    most_common = common_numbers[:1]
    return most_common
    
print(most_frequent(lst))



#%%
#hw question 5
def diff(p):  
    dp = {}   
    lst = p.items()
    
    for key, value in lst:        
        if key != 0:           
            dp[(key -1)] = key * value
    return dp
#%%   
def average_list(n):
    for sublist in inp:


































