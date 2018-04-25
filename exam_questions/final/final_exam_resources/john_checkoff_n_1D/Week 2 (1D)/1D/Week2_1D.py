#!/usr/bin/python
# -*- coding: utf-8 -*-

from pythymiodw import *


def print_temp(t_celcius):
    fahrenheit = (t_celcius*1.8)+32
    a = round(t_celcius,3)
    b = round(fahrenheit,3)
    print ("The temperature in Celsius is", a, "and Fahrenheit is", b)

    return fahrenheit
    """ calculate t_fahrenheit and print both
    """
    pass

def forward(speedleft, speedright, duration):
    """ move both wheels for that duration, and stop
    """
    robot.wheels(speedleft,speedright)
    robot.sleep(duration)
    pass

robot = ThymioReal() # create an object


############### Start writing your code here ################ 

# Prompt user to enter speed and duration of movement
speedleft = int(input("Enter the left throttle value:"))
speedright = int(input("Enter the right throttle value:"))
duration = int(input("Enter the duration:"))

# Move according to the specified speed and duration
forward(speedleft, speedright, duration)

# Read temperature in celcius from the sensor and print it
t_celcius=robot.get_temperature()
print_temp(t_celcius)


########################## end ############################## 

robot.quit() # disconnect the communication

