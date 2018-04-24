# -*- coding: utf-8 -*-
"""
Created on Sun Mar 18 19:07:19 2018

@author: jon_c
"""
#print c.state to see current state
#question 1
from libdw import sm

class CM(sm.SM):
    
    start_state = 0
    
    def get_next_values(self, state, inp):
        next_state = None
        output = None
        
        if(state == 0 and inp == 100):
            next_state = 0 
            output = (0, "coke", 0)
            
        elif(state == 0 and inp == 50):
            next_state = 1
            output = (50, "--", 0)
        
        elif(state == 1 and inp == 100):
            next_state = 0
            output = (0, "coke", 50)
            
        elif(state == 1 and inp == 50):
            next_state = 0
            output = (0, "coke", 0)
        
        else:
            next_state = state
            output = (state, "--", inp)
          
        return next_state, output
        
            
#%%
#question 2
from libdw import sm

class SimpleAccount(sm.SM):
    def __init__(self, start_deposit):
        self.start_state = start_deposit
        
    def get_next_values(self, state, inp):
        if(state < 100 and inp < 0):
            return state + inp -5, state + inp -5
        else:
            return state + inp, state + inp



#%%
#hw question 1
from libdw import sm

class CommentsSM(sm.SM):
    
    start_state = 0

    def get_next_values(self, state, inp):
        
        if(state == 0 and inp != "#"):
           next_state = 0
           output= None
           
       elif(state == 0 and inp == "#"):
            next_state = 1
            output = inp
            
        elif(state == 1 and inp != "\n"):
            next_state = 1
            output = inp
            
        elif(state == 1 and inp == "\n"):
            next_state = 0
            output = None
        
        return next_state, output  


#%%
#hw question 2

from libdw import sm

class FirstWordSM(sm.SM):
    
    start_state = 0

    def get_next_values(self, state, inp):
        
        if(state == 0 and inp != " "):
            next_state = 0
            output = inp
        elif(state == 0 and inp == " "):
            next_state = 2
            output = None
        elif(state == 2 and inp != "\n"):
            next_state = 2
            output = None
        elif(state == 2 and inp == "\n"):
            next_state = 1
            output = None
        elif(state == 1 and inp = " "):
            next_state = 1
            output = None
        elif(state == 1 and inp != " "):
            next_state = 0
            output = inp
           
        return next_state, output  
   
    
#%%
        
from libdw import sm

class SpellCheckSM(sm.SM):
    start_state = "new word"
    def get_next_values(self,state,inp):
        valid_consonant_lst = ["k", "g", "s", "t", "d", "n", "h", "b", "m", "r"]
        valid_vowel_lst = ["a", "e", "i", "o", "u"]
        if (state == "new word" and inp in valid_consonant_lst):
            next_state = "consonant"
            output = ""
        elif (state == "new word" and inp not in valid_consonant_lst and inp != " "):
            next_state = "error"
            output = ""
        elif (state == "new word" and inp == " "):
            next_state = "new word"
            output = ""
        elif (state == "consonant" and inp in valid_vowel_lst):
            next_state = "vowel"
            output = ""
        elif (state == "consonant" and inp != " " and inp not in valid_vowel_lst):
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

print('test case A') 
a = SpellCheckSM() 
line = 'a si tu ne mai me pas je ' 
print(a.transduce(line))

line = 'hi ka ru no de ' 
print(a.transduce(line))

line = 'mu ' 
a.transduce(line,verbose=True)
    
    
    
    

    
    
    
    
    
    
    




















