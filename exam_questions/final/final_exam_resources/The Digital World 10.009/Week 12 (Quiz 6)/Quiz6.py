# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 09:51:43 2018

@author: jon_c
"""

from libdw import sm

#implement your class below

class RunOfOddNumbers(sm.SM):
    
    start_state = "even"
    
    def get_next_values(self, state, inp):
        even = ["2", "4", "6", "8", "10", "12", "14", "16", "18", "20"]
        odd = ["1", "3", "5", "7", "9"]
        
        if (state == "even" and inp in odd):
            next_state = "count"
            output = "1"
        elif (state == "count" and inp in even):
            next_state = "even"
            output = "0"
        elif (state == "count" and inp in odd and output == "1"):
            next_state = "count"
            output = "2"
        elif (state == "count" and inp in odd and output == "2"):
            next_state = "count"
            output = "3"
        elif (state == "count" and inp in odd and output == "3"):
            next_state = 'count"
            output = "4"
        elif (state == "even" and inp in even):
            next_state = "even"
            output = "0"
            
        return next_state, output
    
    #wrong, its a non finite SM
