# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 10:23:05 2018

@author: jon_c
"""
#%%
#question 1
import random

craps=set([2,3,12])
naturals=set([7,11])

def roll_two_dices():
    n1 = random.randrange(1,7)
    n2 = random.randrange(1,7)
    return n1, n2

#print (roll_two_dices())

def print_lose():
    a = print("You lose")
    return a

def print_win():
    a = print("You win")
    return a

def print_point(p):
    #if p == 4 or p == 5 or p == 6 or p == 8 or p == 9 or p == 10:
    #   return True
    a = print ("Your points are", p)
    return a

def is_craps(n):
    #if n in craps:
    if n == 2 or n == 3 or n == 12:
        return True 
 
def is_naturals(n):
    #if n in naturals:
    if n == 7 or n == 1:
        return True

def play_craps():
    point = -1
    while True:
        n1, n2 = roll_two_dices()
        sumn = n1 + n2
        print ('You rolled %d + %d = %d'%(n1,n2,sumn))   
        if point == -1:              
            if is_craps(sumn):  
                print_lose()     
                return 0
            elif is_naturals(sumn):   
                print_win()     
                return 1
            point = sumn
            print_point(point)
        else:
            if sumn == 7:
                print_lose()
                return 0
            elif sumn == point:
                print_win()
                return 1 
print(play_craps())
#%%

#question 2
def leap_year(year):
    if year % 4 == 0 and year % 100 == 0:
        if year % 400 == 0:
            return True
        else:
            return False
    elif year % 4 == 0 and year % 100 != 0:
        return True
    else:
        return False

for x in range(1800,1801):
    print(leap_year(x))
#how to count the number of leap years during a given period?

def bigr(y, x):
    remainder = y % x
    return remainder

def day_of_week_jan1(year):
    if year > 1800 and year < 2099:
        day = bigr(1 + 5 * bigr(year - 1, 4) + 4 * bigr(year - 1, 100) + 6 * bigr(year -1, 400), 7)
        return day

print (day_of_week_jan1(2018))


def num_days_in_month(month_num, leap_year):
    if month_num == 1 or month_num == 3 or month_num == 5 or month_num == 7 or month_num == 8 or month_num == 10 or month_num == 12:
        return 31
    elif month_num == 4 or month_num == 6 or month_num == 9 or month_num == 11:
        return 30
    elif month_num == 2 and leap_year == True:
        return 29
    elif month_num == 2 and leap_year == False:
        return 28

print(num_days_in_month(4, False))

def construct_cal_month(month_num, first_day_of_month, num_days_in_month):
    list = []
    months = {1 : "January", 2 : "February", 3 : "March", 4 : "April", 5 : "May", 6 : "June", 7 : "July", 8 : "August",
              9 : "September", 10 : "October", 11 : "November", 12 : "December"}
    
    list.append(months[month_num])
    
    three_spaces = '   '
    outstr = three_spaces * first_day_of_month
    week_counter = first_day_of_month
    for i in range (1, num_days_in_month + 1):
        outstr += '{:3d}'.format(i)
        week_counter += 1
        if week_counter == 7:
            list.append(outstr)
            week_counter = 0
            outstr = ''
        
    list.append(outstr)
    return list

print(construct_cal_month(1, 5, 31))

#def print_cal_month (list_of_str):
#    ret_val =''
#    for l in list_of_str :
#            ret_val += l. replace (' ','*')
#            ret_val += '\n'
#    return ret_val

#ans = construct_cal_month (1 ,5 ,31)
#print ( print_cal_month (ans))    

def construct_cal_year(year):
    outlist=[]
    outlist.append(year)
    checkleap = leap_year(year)
    day1 = day_of_week_jan1
    
    for month in range(1,13):
        numdays = num_days_in_month(month, checkleap)
        cal_month = construct_cal_month(month, day1, numdays)
        day1 = (day1 + numdays) % 7
        outlist.append(cal_month)
        
    return outlist
        
print(construct_cal_year(2018))

def display_calendar(year):
    calendar = ""
    calendar_year = construct_cal_year(year)
    calendar_year.pop(0)
    for i, month in enumerate(calendar_year):
        for i, week in enumerate(month):
            calendar += week +"\n"
            if i == 0:
                calendar += "  S  M  T  W  T  F  S\n"
        if i !=11:
            calendar += "\n"
    return calendar.strip()
#%%
#question 2 alternative    
def leap_year(year):
    if year%400 == 0:
        return True
    elif year%100 == 0:
        return False
    elif year%4 == 0:
        return True
    else:
        return False
    
def R(y,x):
    return y%x
def day_of_week_jan1(year):
    d = R(1+5*R(year-1,4)+4*R(year-1,100)+6*R(year-1,400),7)
    return d


def num_days_in_month(month_num, leap_year):
    if month_num in [1,3,5,7,8,10,12]:
        return 31
    elif month_num == 2:
        return 29 if leap_year else 28
    else:
        return 30

def construct_cal_month(month_num, first_day_of_month, num_days_in_month):
    month_names = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    calmonth = [month_names[month_num-1]]

    first_day_of_month += 1
    week = [" "*2 for i in range(first_day_of_month-1)]
    
    for i in range(first_day_of_month, num_days_in_month + first_day_of_month):
        week.append(i-first_day_of_month+1)
        
        if i%7 ==0 or i == num_days_in_month + first_day_of_month-1:
            week = " ".join([" " + str(num) if len(str(num)) == 1 else str(num) for num in week])
            calmonth.append(' ' + week)
            week = []
    return calmonth
    
 
def construct_cal_year(year):
    leapyear = leap_year(year)
    firstday = day_of_week_jan1(year)

    calyear = [year]
    for i in range(1,13):
        numdays = num_days_in_month(i,leapyear)
        print(construct_cal_month(i, firstday, numdays))
        calyear.append(construct_cal_month(i, firstday, numdays))
        firstday = (firstday + numdays)%7
    print(calyear)
    return calyear

def display_calendar(year):
    calendar = ""
    calendar_year = construct_cal_year(year)
    calendar_year.pop(0)
    for i, month in enumerate(calendar_year):
        for i, week in enumerate(month):
            calendar += week +"\n"
            if i == 0:
                calendar += "  S  M  T  W  T  F  S\n"
        if i !=11:
            calendar += "\n"
    return calendar.strip()
#%%

#question 3
    
def factorial(n):
    num = 1
    if n <= 1:
        return 1
    else:
        for i in range(n):
            num = num * n
            n = n - 1
    return num

print (factorial(7))


#%%
#question 3 alternative

def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(7))


#%%

#hw question 1
def extract_values(values):
    valuetuple = tuple(map(int, values.split(' ')))
    return valuetuple

def calc_ratios(values):
    i = values[0]
    j = values[1]
    if j == 0:
        return None
    else:
        div = i / j
        return div


def get_integer_ratio():
    data=input('Enter integer pair (hit Enter to quit)')  
    while data !='':
        values=extract_values(data)
        ratio=calc_ratios(values)
        print('The ratio of the two integers are: {:.2f}'.format(ratio))
        data=input('Enter integer pair (hit Enter to quit)')


#%%
        
#hw question 2














