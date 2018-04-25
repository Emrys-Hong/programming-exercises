# -*- coding: utf-8 -*-
"""
Created on Sun Apr 15 16:10:30 2018

@author: jon_c
"""

#question 3
inp = "2 3 40 3 5 4 -3 3 3 2 0"
test = inp.split()
lst = sorted(test)
print(lst)

def maxOccurences(lst):
    counter = 0
    for num, element in enumerate(lst):
        if element == element + 1:
            counter += 1
            
#%%
#question 4
from libdw import sm

class RingCounter(sm.SM):
    start_state = "0"
    def get_next_values(self,state,inp):
        if (inp == 1):
            next_state = "0"
            output = "000"
            
        elif (state == "0" and inp == 0):
            next_state = "1"
            output = "001"
            
        elif (state == "1" and inp == 0):
            next_state = "2"
            output = "010"
            
        elif (state == "2" and inp == 0):
            next_state = "3"
            output = "011"
            
        elif (state == "3" and inp == 0):
            next_state = "4"
            output = "100"
            
        elif (state == "4" and inp == 0):
            next_state = "5"
            output = "101"
            
        elif (state == "5" and inp == 0):
            next_state = "6"
            output = "110"
            
        elif (state == "6" and inp == 0):
            next_state = "7"
            output = "111"
        
        elif (state == "7" and inp == 0):
            next_state = "0"
            output = "000"
        
        return next_state, output

print ("test 1")
r=RingCounter()
print (r.transduce([0,0,0,0,0,0,0,0,0]))

print ("test 2")
r=RingCounter()
print (r.transduce([0,0,0,1,0,0,0,0,0]))

print ("test 3")
r=RingCounter()
print (r.transduce([0,0,0,1,0,0,1,0,0]))
#%%        
#question 5
class Avatar:
    def __init__(self, name = (), hp = 100, position = (1,1)):
        self.name = name #string
        self.hp = hp #integer
        self.position = position #tuple
    
    def getName(self):
        return self.name
        
    def setName(self, name):
        self.name = name
        
    Name = property(getName, setName)
    
    def getHP(self):
        return self.hp
        
    def setHP(self, hp):
        self.hp = hp
        
    HP = property(getHP, setHP)    
    
    def getPosition(self):
        return self.position
        
    def setPosition(self, position):
        self.position = position
     
    Position = property(getPosition, setPosition)
    
    def heal(self, h = 1):
        if h < 0:
            self.hp
        else:
            self.hp += h
        
    def attacked(self, a = -1):
        if a > 0:
            self.hp 
        else: 
            self.hp += a
        
print ("test 1: __init__")
a = Avatar("John")
print (a.name, a.hp, a.position)

print ("test 2: __init__")
a = Avatar("Jane", 150, (10,10))
print (a.name, a.hp, a.position)

print ("test 3: getName(), setName()")
a = Avatar("John")
a.setName("Jude")
print (a.getName())       
                    
print ("test 4: getPosition(), setPosition()")
a = Avatar("John")
a.setPosition((1, 3))
print (a.getPosition())

print ("test 5: getHP(), setHP()")
a = Avatar("John")
a.setHP(200)
print (a.getHP())

print ("test 6: heal()")
a = Avatar("John")
a.heal(5)
print (a.getHP())

print ("test 7: attacked()")
a = Avatar("John")
a.attacked(20)
print (a.getHP())

print ("test 8: heal()")
a = Avatar("John")
a.heal()
print (a.getHP())

print ("test 9: attacked()")
a = Avatar("John")
a.attacked()
print (a.getHP())

print ("test 10: heal(), attacked()")
a = Avatar("John")
a.attacked(2)
a.heal(-2)
print (a.getHP())           
            
#%%
#question 6
class Map:
    def __init__(self, world):
        self.world = world
       
    def whatIsAt(self, keywhat):
        if keywhat not in self.world.keys():
            return ("Empty")
        elif keywhat in self.world.keys():
            if self.world[keywhat] == "x":
                return ("Exit")
            elif self.world[keywhat] == 0:
                return ("Wall")
            elif self.world[keywhat] > 0:
                return ("Food")
            elif self.world[keywhat] < 0:
                return ("Enemy")
       
    
    def getEnemyAttack(self, keyenemy):
        if keyenemy not in self.world.keys():
            return False
        elif keyenemy in self.world.keys():
            return self.world[keyenemy]
        

    def getFoodEnergy(self, keyfood):
        if keyfood not in self.world.keys():
            return False
        elif keyfood in self.world.keys():
            return self.world[keyfood]
        

    def removeEnemy(self, keyremove):
        if keyremove not in self.world.keys():
            return False
        elif keyremove in self.world.keys():
            self.world.pop(keyremove)
            return True
            
    
    def eatFood(self, keyeat):
        if keyeat not in self.world.keys():
            return False
        elif keyeat in self.world.keys():
            self.world.pop(keyeat)
            return True
    
    def getExitPosition(self):
        for key, value in self.world.items():
            if value == "x":
                return key
            
            
world = {(0,0):0, (1,0):0 , (2,0):0, (3,0): 0, (4,0):0, (5,0): 0,
(0,1):0, (1,1): 2, (2,1):-3, (5,1): 0, (0,2):0, (5,2): 0, (0,3):0,
(5,3): 0, (0,4):0, (5,4): 0, (0,5):0, (1,5):0 , (2,5):0, (3,5): 0,
(4,5):"x", (5,5): 0}

print ("test 1: object instantiation")
m=Map(world)
print (m.world)

print ("test 2: whatIsAt")
print (m.whatIsAt((1,0)))

print ("test 3: whatIsAt")
print (m.whatIsAt((2,1)))

print ("test 4: whatIsAt")
print (m.whatIsAt((1,1)))

print ("test 5: getFoodEnergy")
w1 = m.getFoodEnergy((1,1))
w2 = m.getFoodEnergy((3,3))
print (w1, w2)

print ("test 6: getEnemyAttack")
w1 = m.getEnemyAttack((2,1))
w2 = m.getEnemyAttack((3,3))
print (w1, w2)

print ("test 7: removeEnemy")
w1 = m.getEnemyAttack((2,1))
w2 = m.removeEnemy((2,1))
w3 = m.getEnemyAttack((2,1))
print (w1,w2,w3)

print ("test 8: whatIsAt")
print (m.whatIsAt((1,4)))

print ("test 9: getFoodEnergy")
print (m.getFoodEnergy((1,4)))

print ("test 10: getEnemyAttack")
print (m.getEnemyAttack((1,4)))

print ("test 11: whatIsAt")
print (m.whatIsAt((4,5)))

print ("test 12: getExitPosition")
print (m.getExitPosition())

print ("test 13: eatFood")
w1 = m.whatIsAt((1,1))
w2 = m.eatFood((1,1))
w3 = m.whatIsAt((1,1))
print (w1,w2,w3)

print ("test 14: test aliasing")
print (m.world == world)        
            
#%%
#question 7
from libdw import sm

class DW2Game(sm.SM):
    
    def __init__(self, Avatar, Map):
        self.Avatar = Avatar
        self.Map = Map
        startState = (self.Avatar, self.Map)
        
    def getNextValues(current_state, inp):
        
    
    
    
    
            
            
            
            
            
            
            
