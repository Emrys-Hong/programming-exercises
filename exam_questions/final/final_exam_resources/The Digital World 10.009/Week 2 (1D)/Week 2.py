# -*- coding: utf-8 -*-
"""
Created on Sun Feb 18 21:49:05 2018

@author: jon_c
"""

import turtle 
wn = turtle.Screen()
wn.bgcolor("lightgreen")
wn.title("Welcome")

wn.textinput("Name", "Name of player?")
alex = turtle.Turtle()
alex.color("hotpink")
alex.pensize(5)
alex.forward(50)
alex.left(90)
alex.forward(3)

james = turtle.Turtle()
james.left(90)
james.forward(100)

tess = turtle.Turtle()
tess.back(100)

wn.exitonclick()

#1. Modify this program so that before it creates the window, it prompts the user to enter
#the desired background color. It should store the user’s responses in a variable, and
#modify the color of the window according to the user’s wishes. (Hint: you can find a list
#of permitted color names at http://www.tcl.tk/man/tcl8.4/TkCmd/colors.htm. It includes
#some quite unusual ones, like “peach puff” and “HotPink”.)
#2. Do similar changes to allow the user, at runtime, to set tess‘ color.
#3. Do the same for the width of tess‘ pen. Hint: your dialog with the user will return a
#string, but tess‘ pensize method expects its argument to be an int. So you’ll need to
#convert the string to an int before you pass it to pensize.



for f in ["Joe","Zoe","Brad","Angelina","Zuki","Thandi","Paris"]:
    invite = "Hi " + f + ". Please come to my party on Saturday!"
    print(invite)


for i in range(3, 6):
    test = 123
    print (test)

    
import turtle 
wn = turtle.Screen()
wn.bgcolor("lightgreen")
wn.title("Welcome")

wn.textinput("Name", "Name of player?")
alex = turtle.Turtle()
alex.color("hotpink")
for c in ["black", "red", "purple", "blue"]:
    alex.color(c)
    alex.forward(50)
    alex.left(90)
    
wn.exitonclick()
    

import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")
alex = turtle.Turtle()
alex.shape("turtle")
alex.color("blue", "yellow")

#alex.penup()
size = 20
colors = ["black", "red", "yellow", "blue"]
for colors in range (30):
    alex.stamp()
    size = size + 3
    alex.forward(size)
    alex.right(24)
    
wn.mainloop()
#yo, how to make the turtle change color with each
#step?




def hello():
    print ("Hello World!")
    
hello()    

def name():
    print ('jon')
    
name()    

def add_numbers(x, y, z):
    a = x + y
    b = x + z
    c = y + z
    print (a, b, c)

add_numbers(1, 2, 3)

def names():
    name = str(input("Enter your name:"))
    if set ("aeiou").intersection(name.lower()):
        print ("Your name has a vowel")
    else:
        print ("Your name does not have a vowel")
        
    for letter in name:
        print (letter)
        
names()


import turtle

def draw_square (t, sz):
    for i in range(4):
        t.forward(sz)
        t.left(90)
        
wn = turtle.Screen()
wn.bgcolor("lightgreen")
wn.title("Alex meets a function")

alex = turtle.Turtle
draw_square (alex, 50)
wn.mainloop()


import turtle

def draw_multicolor_square(t, sz):
    for i in ["red", "purple", "hotpink", "blue"]:
        t.color(i)
        t.forward(sz)
        t.left(90)

wn = turtle.Screen() # Set up the window and its attributes
wn.bgcolor("lightgreen")

tess = turtle.Turtle() # Create tess and set some attributes
tess.pensize(3)

size = 20 # Size of the smallest square
for i in range(15):
    draw_multicolor_square(tess, size)
    size = size + 10 # Increase the size for next time
    tess.forward(10) # Move tess along a little
    tess.right(18) # and give her some turn

wn.mainloop()


def final_amt(p, r, n, t):
    a = p * (1 + (r/n))**(n*t)
    return a

toInvest = float(input("How much do you want to invest?"))
fnl = final_amt(toInvest, 0.08, 12, 5)
print ("At the end of the period you'll have", fnl)



def next_function(a):
    a = 8
    return a
a = 20
print ( next_function (a))

unit = 100
currency = "JPY"
rate = 1.183

money_changer = "we sell {0:6d} {1:>10s} at {2:4.3f} SGD".format(unit, currency, rate)
print(money_changer) 
#above is to force a return value with a certain number of decimals or spaces