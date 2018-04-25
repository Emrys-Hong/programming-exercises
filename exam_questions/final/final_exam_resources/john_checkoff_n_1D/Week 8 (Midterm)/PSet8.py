# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 12:55:14 2018

@author: jon_c
"""

#question 1
import math

class Coordinate:
    
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
    
    def magnitude(self):
        mag = math.sqrt(self.x**2 + self.y**2)
        return mag
    
    def translate(self, dx, dy):
        self.x = self.x + dx
        self.y = self.y + dy
    
    def __eq__(self, other):
        is_x_equal = self.x == other.x
        is_y_equal = self.y == other.y
        return is_x_equal and is_y_equal
    
    def __str__(self):
        output = "x = " + str(self.x) + ",y = " + str(self.y)
        return output
    
    def __lt__(self, other):
        is_x_less = self.x < other.x
        is_y_less = self.y < other.y
        return is_x_less and is_y_less
    
p = Coordinate()                                                                                                                                                   
p.x = 3                                                                                                                                                            
p.y = 4                                                                                                                                                            
print(p.magnitude())
p = Coordinate(3, 4)                                                                                                                                               
q = Coordinate(4, 6)                                                                                                                                               
print(p==q)
#%%
#question 2
class Celsius:
    
    def __init__(self, temp = 0):
        self._temperature = temp

    def to_fahrenheit(self):
        american = (self._temperature * (9 / 5)) + 32
        return american
    
    '''getter'''
    def get_temperature(self):
        return self._temperature
    
    '''setter:takes care of validity'''
    def set_temperature(self, t):
        if (t < -273):
            self._temperature = -273
        else:
            self._temperature = t
    
    temperature = property(get_temperature, set_temperature)
    
    
#%%
#question 3
import time
class StopWatch:
    
    def __init__(self, start_time, end_time):
        self.start_time = start_time
        self.end_time = end_time
        
    def start(self):
        self.start_time = time.clock()
        self.end_time = -1
    
    def stop(self):
        self.end_time = time.clock()
        
    def elapsed_time(self):
        if self.end_time == -1:
            return None
        else:
            elapsed = self.end_time - self.start_time
            return round(elapsed, 1)
        
#%%
#question 4
import numpy as np
class Line:
    
    def __init__(self, c0, c1):
        self.c0 = c0
        self.c1 = c1
    
    def __call__(self, x):
        return (self.c0 + (self.c1 * x))

    
    def table(self, L, R, n):
        xvalues = np.linspace(L, R, n)
        blanktable = []
        
        for i in xvalues:       
            blanktable.append('{:10.2f}'.format(i) + '{:10.2f}'.format(self.c0 + self.c1*i))
            table = '\n'.join(j for j in blanktable) + '\n'
            
        return str(table)      
        

        
        
#%%
#hw question 1
class Time:
    
    def __init__(self, hours, minutes, seconds):
        self._hours = hours
        self._minutes = minutes
        self._seconds = seconds
        
    def get_elapsed_time(self):
        return ((self._hours * 3600) + (self._minutes * 60) + self._seconds)
        

    def set_elapsed_time(self, x):
        if x >= 86400:
            x = x % 86400
            self._hours = x // 3600
            self._minutes = (x % 3600) // 60
            self._seconds = x % 3600 % 60
        else:
            self._hours = x // 3600
            self._minutes = (x % 3600) // 60
            self._seconds = x % 3600 % 60
                
        
    def __str__(self):
        return "Time: {}:{}:{}".format(self._hours, self._minutes, self._seconds)
    
        
    elapsed_time = property(get_elapsed_time, set_elapsed_time)

t = Time(100, 19, 10)
print(t.elapsed_time)
print(t)
#%%
#hw question 1 Kevin's answer
class Time:
    
    def __init__(self, hours, minutes, seconds):
        self._hours = hours
        self._minutes = minutes
        self._seconds = seconds
        
    def get_elapsed_time(self):
        return ((self._hours * 3600) + (self._minutes * 60) + self._seconds)
        

    def set_elapsed_time(self, x):
        self._hours = ((x // 60) // 60) % 24
        self._minutes = ((x - (60 * 60 * self._hours)) // 60) % 60   
        self._seconds = ((x - (60 * 60 * self._hours) - (60 * self._minutes)) % 60)
                
        
    def __str__(self):
        return "Time: {}:{}:{}".format(self._hours, self._minutes, self._seconds)
    
        
    elapsed_time = property(get_elapsed_time, set_elapsed_time)
    
t = Time(100, 19, 10)
print(t.elapsed_time)
t.elapsed_time = 1000
print(t.elapsed_time)
print(t)
#%%
#hw question 2
class Account:    
    
    def __init__(self, owner, account_number, amount):
        self._owner = owner
        self._account_number = account_number
        self._balance = amount

    def deposit(self, amount):
        self._balance += amount
    
    def withdraw(self, amount):
        self._balance -= amount
    
    def __str__(self):
        return "{}, {}, balance: {}".format(self._owner, self._account_number, self._balance)
    
    
class test:
    def __init__(Account, ):
        super().__init__()

       
#%%
#hw question 3
class Diff:
    
    def __init__(self, f, h = 10 ** (-4)):
        self.f = f
        self.h = h
                 
    def __call__(self, x):
        return (self.f(x + self.h) - self.f(x)) / self.h
        
      
#%%
#question 4
class Polynomial:
    
    def __init__(self, coefficients):
        self.coeff = coefficients
    
    def __add__(self,other):
        if len(self.coeff) < len(other.coeff):
            while len(self.coeff) < len(other.coeff):
                self.coeff.append(0)
        if len(other.coeff) < len(self.coeff):
            while len(other.coeff) < len(self.coeff):
                other.coeff.append(0)
        lst = [i+j for i, j in zip(self.coeff,other.coeff)]
        return Polynomial(lst)
    
    def __sub__(self,other):
        if len(self.coeff) < len(other.coeff):
            while len(self.coeff) < len(other.coeff):
                self.coeff.append(0)
        if len(other.coeff) < len(self.coeff):
            while len(other.coeff) < len(self.coeff):
                other.coeff.append(0)
        lst = [i-j for i, j in zip(self.coeff,other.coeff)]
        return Polynomial(lst)
    
    def __call__(self, x):
        result = 0
        for i in range(len(self.coeff)):
            result += self.coeff[i] * x ** i
        return result
    
    def __mul__(self,other):
        res = []
        for i in range(len(self.coeff) + len(other.coeff)):
            res.append(0)
        for i, c in enumerate(self.coeff):
            for j, o in enumerate(other.coeff):
                res[i + j] += c * o
        while res[-1] == 0:
            res.pop()
        return Polynomial(res)

    def differentiate(self):
        new_coeffs = []
        for i in range(len(self.coeff)):
            try:
                c = self.coeff[i+1]
                new_coeffs.append((i + 1) * c)
            except:
                pass
        self.coeff = new_coeffs
        return None

    def derivative(self):
        new_coeffs = []
        for i in range(len(self.coeff)):
            try:
                c = self.coeff[i+1]
                new_coeffs.append((i + 1) * c)
            except:
                pass
        return Polynomial(new_coeffs)




#%%
#exercise question 1
import math
class F:
    
    def __init__(self, a, w):
        self._a = a
        self._w = w
        
    def __call__(self, x): 
        return (math.e ** (-self._a * x)) * (math.sin(self._w * x))

f = F(a=1.0 , w =0.1)
print (f(x=math.pi))
f = F(a=3.0 , w =0.5)
print (f(x=math.pi/2))
f = F(a=5.0 , w =1.5)
print (f(x=math.pi/4))
f = F(a=5.0 , w =2.0)
print (f(x=math.pi/6))
f = F(a=10.0 , w =3.0)
print (f(x=math.pi/18))

#%%
#exercise question 2
class Line0:
    
    def __init__(self, p1, p2):
        self._p1 = p1
        self._p2 = p2
        
    def __call__(self, x):
        grad = (self._p2[1] - self._p1[1]) / (self._p2[0] - self._p1[0])
        intercept = self._p1[1] - grad * self._p1[0]
        return ((grad * x) + intercept)
    
#%%


        





















    
    
    
    
    