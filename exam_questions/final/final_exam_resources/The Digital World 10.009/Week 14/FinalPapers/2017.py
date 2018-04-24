# -*- coding: utf-8 -*-
"""
Created on Sun Apr 15 11:41:16 2018

@author: jon_c
"""
#question 3
def complete_ISBN(inp):
    checksum = (int(inp[0]) * 1 + int(inp[1]) * 2 + int(inp[2]) * 3 + int(inp[3]) * 4 + int(inp[4]) * 5 + int(inp[5]) * 6 + 
                int(inp[6]) * 7 + int(inp[7]) * 8 + int(inp[8]) * 9) % 11
    if checksum == 10:
        isbn = inp + "X"
    else:
        isbn = inp + str(checksum)
    return isbn


inp = "013601267"
inp2 = "013031997"
inp3 = "020139829"
print(complete_ISBN(inp))    
print(complete_ISBN(inp2))    
print(complete_ISBN(inp3))    
#%%
#question 4
inlist = [(3,5),(2,2),(2,2,3),(12,2),(7,3),(3,7,1)]

def get_products(inlist, test):
    d = {}
    o = []
    for tuples in inlist:
        product = 1
        for elements in tuples:
            product = product * elements
        d[product] = [tuples]   #to create new key & value. can be done without putting tuples in a list    
        if test == product:
            o.append(tuples)
#        elif test != product:
#            pass
    return d, o
    


d, o = get_products(inlist, 15)
print(get_products(inlist, 15))
print(sorted(d.keys()))
print(sorted(d.values()))
print(o)

d, o = get_products(inlist, 21)
print(o)

d, o = get_products(inlist, 11)
print(o)
#%%
#dictionary lesson 
dct = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
print (dct['Name'])
print (dct['Age'])

dct['Age'] = 8; # update existing entry
dct['School'] = "DPS School"; # Add new entry

print (dct['Age'])
print(dct['School'])
dct.clear()
print(dct)

dct = {'Name': 'Zara', 'Age': 7, 'Class': 'First'} #delete an entry
dct.pop("Name")
print(dct)
#%%
#question 5
from libdw import sm

class SpellCheckSM(sm.SM):
    start_state = "new word"
    def get_next_values(self,state,inp):
        consonantlst = ["k" "g" "s" "t" "d" "n" "h" "b" "m" "r"]
        vowellst = ["a", "e", "i", "o", "u"]
        if (state == "new word" and inp in consonantlst):
            next_state = "consonant"
            output = ""
        elif (state == "new word" and inp not in consonantlst and inp != " "):
            next_state = "error"
            output = ""
        elif (state == "new word" and inp == " "):
            next_state = "new word"
            output = ""
        elif (state == "consonant" and inp in vowellst):
            next_state = "vowel"
            output = ""
        elif (state == "consonant" and inp != " " and inp not in vowellst):
            next_state = "error"
            output = ""
        elif (state == "consonant" and inp == " "):
            next_state = "new word"
            output = "error"
        elif (state == "vowel" and inp == " "):
            next_state = "new word"
            output = "ok"
        elif (state == "vowel" and inp != " "):
            next_state = "error"
            output = ""
        elif (state == "error" and inp != " "):
            next_state = "error"
            output = ""
        elif (state == "error" and inp == " "):
            next_state = "new word"
            output = "error"
            
        return next_state, output
    
print ('test case A')
a = SpellCheckSM() 
line = 'a si tu ne mai me pas je ' 
print (a.transduce(line))

print ('test case B')
a = SpellCheckSM() 
line = 'hi ka ru no de ' 
print (a.transduce(line))

print ('test case C') 
a = SpellCheckSM() 
line = 'mu ' 
print (a.transduce(line,verbose=True))

    
#%%
#question 6 part a
class Parallelogram:
    
    def __init__(self, side1, side2, diagonal):
        self.side1 = side1
        self.side2 = side2
        self.diagonal = diagonal
        
    def __str__(self):
        return str("%.2f" % self.diagonal)
    
para = Parallelogram(2,3,4)
print (para)

#%%
#question 6 part b
class Parallelogram:
    
    def __init__(self, side1, side2, diagonal):
        self.side1 = side1
        self.side2 = side2
        self.diagonal = diagonal                
        
    def __str__(self):
        return str("%.2f" % self.diagonal)
    
    def get_diagonal(self):
        return self._diagonal
        
    def set_diagonal(self, d):
        if d < 0:
            self._diagonal = 0
        else:
            self._diagonal = d 
            
    diagonal = property(get_diagonal, set_diagonal)
            
para = Parallelogram(2,3,4)
para.diagonal = 3
print(para)

para = Parallelogram(2,3,4)
para.diagonal = -1
print (para)

''' i only get the answer if i make the self._diagonal private, why is that?'''
#%%
#question 6 part c
from math import sqrt
class Parallelogram:
    
    def __init__(self, side1, side2, diagonal):
        self.side1 = side1
        self.side2 = side2
        self._diagonal = diagonal                
        
    def __str__(self):
        return str("%.2f" % self.diagonal)
    
    def get_diagonal(self):
        return self._diagonal
        
    def set_diagonal(self, d):
        if d < 0:
            self._diagonal = 0
        else:
            self._diagonal = d 
            
    diagonal = property(get_diagonal, set_diagonal)
    
    def __call__(self):
        if self.side1 + self.side2 > self._diagonal:
            return True
        else:
            return False
    
class Rhombus(Parallelogram): 
    def __call__(self):
        if self.side1 == self.side2:
            return True
        else:
            return False
    
class Rectangle(Parallelogram):    
    def __call__(self):
        if (self.side1 ** 2 + self.side2 ** 2) == self._diagonal:
            return True
        else:
            return False


class Square(Parallelogram):  
    def __call__(self):
        if self.side1 == self.side2 and sqrt(self.side1 ** 2 + self.side2 ** 2) == self._diagonal:
            return True
        else:
            return False
        
para = Parallelogram(3,4,5)
print (para())

para = Parallelogram(3,4,8)
print (para())

rect = Rectangle(3,4,6)
print (rect())

rhom = Rhombus(3,3,2)
print (rhom())

squr = Square(2,2,3)
print (squr())

squr = Square(2,2,sqrt(8))
print (squr())
    
#%%    
#question 6 part d
from math import sqrt
class Parallelogram:
    
    def __init__(self, side1, side2, diagonal):
        self.side1 = side1
        self.side2 = side2
        self._diagonal = diagonal                
        
    def __str__(self):
        return str("%.2f" % self.diagonal)
    
    def get_diagonal(self):
        return self._diagonal
        
    def set_diagonal(self, d):
        if d < 0:
            self._diagonal = 0
        else:
            self._diagonal = d 
            
    diagonal = property(get_diagonal, set_diagonal)
    
    def __call__(self):
        if self.side1 + self.side2 > self._diagonal:
            return True
        else:
            return False
        
    def calc_area(self):
        s = (self.side1 + self.side2 + self._diagonal) / 2
        return round((2 * sqrt(s * (s - self.side1 ) * (s - self.side2) * (s - self._diagonal))), 2)
        
    
class Rhombus(Parallelogram): 
    def __call__(self):
        if self.side1 == self.side2:
            return True
        else:
            return False
    
    def calc_area(self):
        otherdiagonal = 2 * (sqrt(self.side1 ** 2 - ((self._diagonal / 2) ** 2)))         
#        super().calc_area(self)
        return round(((self._diagonal * otherdiagonal) / 2), 2)
        
    
class Rectangle(Parallelogram):    
    def __call__(self):
        if (self.side1 ** 2 + self.side2 ** 2) == self._diagonal:
            return True
        else:
            return False
        
    def calc_area(self):
#        super().calc_area(self)
        return round((self.side1 * self.side2), 2)
        

class Square(Parallelogram):  
    def __call__(self):
        if self.side1 == self.side2 and sqrt(self.side1 ** 2 + self.side2 ** 2) == self._diagonal:
            return True
        else:
            return False
        
    def calc_area(self):
#        super().calc_area(self)
        return round((self.side1 * self.side2), 2)
        
para = Parallelogram(3,4,2)
print (para.calc_area())

para = Parallelogram(5,7,9)
print (para.calc_area())

rect = Rectangle(3,4,5)
print (rect.calc_area())

rhom = Rhombus(3,3,4)
print (rhom.calc_area())

squr = Square(2,2,2.83)
print (squr.calc_area())



#%%
#question 7
def procrastination(assignments):
    

class MyTask(object):
    def __init__(self, deadline, duration):
        self.deadline = deadline
        self.duration = duration
        
    def __str__(self):
        return "T(%d , %d)" % (self.deadline, self.duration)


assignments = [ MyTask(9,1), MyTask(9,2), MyTask(7,1) ]
print (procrastination(assignments))
assignments1 = [ MyTask(3,2), MyTask(3,2) ]
print (procrastination(assignments1))
assignments2 = [ MyTask(9,1), MyTask(9,2), MyTask(4,3) ]
print (procrastination(assignments2))
assignments3 = [MyTask(14,10), MyTask(33,2), MyTask(5,3), MyTask(14,1), MyTask(10,2)]
print (procrastination(assignments3))
