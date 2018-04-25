# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 12:52:51 2018

@author: jon_c
"""
print("Question 1")
print(type("This is the first Week!"))
print("This is the first Week!")
print(type(24))
print(24)
print(type(2.4))
print(2.4)
print(type("24"))
print("24")
print(type('2.4'))
print(type("""2.4"""))
print(type('''2.4'''))
print(10300)
print(10,300)
print(10.300)
print(type(10.300))

print("Question 2")
print(int(1.1))
print(int(9.81))
print(int(-9.81))
#print(int("9.81")) NO GO M8
#print(int("9.81m/s2")) NO GO M8
print(float("9.81"))
print(str(9.81))
print(type(str(9.81)))
print(str(int(9.81)))
print(type(str(int(9.81))))

print("Question 3")
message = "What's up, Doc?"
n = 17
pi = 3.14159
pi = 3.14

print(message)
print(n)
print(pi)


print("Question 5")
class Coordinate:
    x = 3.2
    y = -1.5
p1 = Coordinate ()
p2 = Coordinate ()
p2.x = 0.3
p2.y = 1.0

print(type(p1))
print(type(p2))
print(type(Coordinate))
print(p1.x, p1.y)
print(p2.x, p2.y)
    
print("Question 6")
print(5 + 3)
print(5 - 3)    
print(5 * 3)
print(5 ** 3)
print(5 / 3)
print(5 // 3)
print(5 / 3.0)
print(5.0 / 3)
print(5 % 3)

print("Question 7")
print(17 - (3 * 7)//(4+1))
print((2**2**4) * 3)

print("Question 8")
x = 3
print (x,end=' ')
x = x + 2
print (x)

x = 3
print (x,end=' ')
x -= 2
print (x)

x = 3
print (x,end=' ')
x *= 2
print (x)


#Question 9a
name = input ('What is your name?')
print (name)
matric = input ('What is your student ID?')
print (matric)
quiz = int(input ('Quiz Score'))
print (quiz)
project = int(input ('Project Score'))
print (project)
final = int(input ('Finals Score'))
print (final)
avg = ((quiz + project + final)/3)
print ('Name:', name)
print ('ID:', matric)
print ('Average:', avg)

#Question 9b
name = input ('What is your name?')
print (name)
matric = input ('What is your student ID?')
print (matric)
quiz = int(input ('Quiz Score'))
print (quiz)
project = int(input ('Project Score'))
print (project)
final = int(input ('Finals Score'))
print (final)
avg = ((quiz + project + final)/3)
print ('Name:', name)
print ('ID:', matric)
print ('Average:', avg)
if avg >= 50:
    print ("Pass")
else:
    print ("Fail")

#Question 9c
name = input ('What is your name?')
print (name)
matric = input ('What is your student ID?')
print (matric)
quiz = int(input ('Quiz Score'))
print (quiz)
project = int(input ('Project Score'))
print (project)
final = int(input ('Finals Score'))
print (final)
avg = ((quiz + project + final)/3)
print ('Name:', name)
print ('ID:', matric)
print ('Average:', avg)
if avg >= 90:
    print ('Grade:',"A")
elif avg >= 80:
    print ('Grade:',"B")
elif avg >= 70:
    print ('Grade:',"C")
elif avg >= 60:
    print ('Grade:',"D")
elif avg < 60:
    print ('Grade:',"F")

#Question 9d
for A in range(40):
    name = input ('What is your name?')
    print (name)
    matric = input ('What is your student ID?')
    print (matric)
    quiz = int(input ('Quiz Score'))
    print (quiz)
    project = int(input ('Project Score'))
    print (project)
    final = int(input ('Finals Score'))
    print (final)
    avg = ((quiz + project + final)/3)
    print ('Name:', name)
    print ('ID:', matric)
    print ('Average:', avg)
    if avg >= 90:
        print ('Grade:',"A")
    elif avg >= 80:
        print ('Grade:',"B")
    elif avg >= 70:
        print ('Grade:',"C")
    elif avg >= 60:
        print ('Grade:',"D")
    elif avg < 60:
        print ('Grade:',"F")

        
for B in range(2, 20, 3):
    print ("wow")




def square(x):
    y = x ** 2
    return y

result = square(3)
print (result)

print ("hanoi")
print ("hotels")

print ("hanoi", end=":")
print ("hotels")

#escpae sequences
print ('poke\nmon')
print ("pika\tchuuu")

