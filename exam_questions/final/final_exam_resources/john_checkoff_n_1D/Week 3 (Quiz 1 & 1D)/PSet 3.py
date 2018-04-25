# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 11:20:31 2018

@author: jon_c
"""

#question 1
def is_larger(n1,n2):
    if n1 > n2:
        result = True
    else:
        result = False
        
    return result

print(is_larger(5,2))

#question 2
def letter_grade(mark):
    if type(mark) != int:
        return None
    elif mark > 100 or mark < 0:
        return None
    elif mark >= 90:
        return ("A")
    elif mark >= 80:
        return ("B")
    elif mark >= 70:
        return ("C")
    elif mark >= 60:
        return ("D")
    else:
        return ("E")

#question 3
def list_sum(ls):
    total = 0
    n = 0
    while n < len(ls):
        total = total + ls[n] 
        n = n + 1
    return total   

#question 3 alternative

def list_sum1(ls):
    if ls == []:
        return 0.0
    else:
        total = 0      
        n = 0
        while n < len(ls):
            total += ls[n]
            n += 1
        return total

print (list_sum1([1,2,3,4,5]))
print (list_sum1([]))
        


#question 4
def minmax_in_list(ls):
    if not ls:
        return (None, None)
    #min
    x = ls[0]
    for  element in ls:
        if element <= x:
            x = element
        else:
            x = x
    
    #max
    y = ls[0]
    for element in ls:
        if element >= y:
            y = element
        else:
            y = y
    return (x,y)

#question 4 alternative
def minmax_in_list1(ls):
    if ls == []:
        return (None, None)
    else:
        n = 0
        min = ls[0]
        max = ls[0]
        while n < len(ls):
            if ls[n] > max:
                max = ls[n]
                n += 1
            elif ls[n] < min:
                min = ls[n]
                n += 1
            else:
                n += 1
        return (min, max)
    
print (minmax_in_list1([1,2,3,4,5,10, 10]))


#question5
def is_palindrome(num):
    if str(num) == str(num)[::-1]:
        return True
    else:
        return False
    
    
    
    
#hwquestion 1    
def check_value(n1,n2,n3,x):
    if n1 < x and n2 < x and n3 > x:
        return True
    else:
        return False
        
    
#hwquestion 2
def temp_convert(choice, temp):
    if choice == "C":
        centigrade = C*float(9)/5 + 32
        return centigrade
    elif choice == "F":
        fahrenheit = (F-32)*float(5)/9
        return fahrenheit

C = 10
F = 10

#hwquestion 3
def get_even_list(ls):
    even = []
    for x in ls:
        if x % 2 == 0:
            even.append (x)
    return even

#question 3 alternative
def get_even_list1(ls):
    newlist = []
    n = 0
    while n < len(ls):
        if ls[n] % 2 == 0:
            newlist.append(ls[n])
            n += 1
        else:
            n += 1
    return newlist

print (get_even_list1([1,2,3,4,5,6,7,8]))


#hwquestion 4
def is_prime(n):    
    if n > 1:
        for x in range(2, n):
            if (n % x) == 0:
                return False
        return True
    else:
        return False

    
#hwquestion 5            
import math
def approx_ode(h,t0,y0,tn):
    y= y0
    t= t0
    while t + (10**-6) <= tn:
        y += h*f(t, y)
        t += h
    y = round (y, 3)
    return y
######### h - step size
######### t0 - initial t value (at step 0)
######### y0 - initial y value (at step 0)
######### tn - t value at step n

######### Add you code below this line
######### Return your answer correct to 3 decimal places
    pass

######### Ignore code below this line ######################################

def f(t, y):
    return 3.0+math.exp(-t)-0.5*y

   
#exercise question 1
def may_ignore(x):
    if type(x) != int:
        return None
    else:
        y = x + 1
        return y
 
    
#exercise question 2
def my_reverse(list1):
    reverse = []
    for i in list1[::-1]:
        reverse.append(i)
    return reverse


#exercise question 2 (alternative)
list1 = [1,2,3,4,5]
def my_reverse1(list1):
    
    reverselist = []
    i = 0
    while i < len(list1):
        reverselist.append(list1[-i-1])
        i += 1
    return reverselist

print (my_reverse1(list1))
    
#exercise question 3
def approx_pi(n):
    i = 0
    summ = 0
    while i < n:
        summ += ((math.factorial(4 * i)) * (1103 + (26390 * i))) / ((math.factorial(i)**4) * 396 **(4 * i))
        i += 1
    inversepi = ((2 * math.sqrt(2)) / 9801) * summ
    pi = 1 / inversepi 
    return pi
    
#exercise question 4

























