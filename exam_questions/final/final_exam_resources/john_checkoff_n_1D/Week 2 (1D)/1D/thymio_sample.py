from pythymiodw import *

robot = ThymioReal() # create an object

robot.wheels(100, 100) # make the robot move at same speed on both wheels
robot.sleep(5) # wait for 5 seconds

robot.wheels(-50, 0) # make the robot turn counter-clockwise with left moving
robot.sleep(2) # wait for 2 seconds

robot.leds_top(0,0,32) # turn on the top LED
robot.sleep(2) # wait for 2 seconds
robot.leds_circle(led0=32) # turn on the circle LED on the top
robot.sleep(2) # wait for 2 seconds

robot.quit() # disconnect communication

robot.get_temperature(A)
print("The temperature reading in Celsius is", A)

