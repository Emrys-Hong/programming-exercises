import RPi.GPIO as GPIO
from pythymiodw import *
from time import sleep
from firebase import firebase

url = 'https://dw-1d-b57fd.firebaseio.com/' # URL to Firebase database
token = 'njrn9ydmOZK8q3z7kTycgl1t5VIqAhAcRua8aj92' # unique token used for authentication

# Create a firebase object by specifying the URL of the database and its secret token.
# The firebase object has functions put and get, that allows user to put data onto 
# the database and also retrieve data from the database.
firebase = firebase.FirebaseApplication(url, token)

# Use the BCM GPIO numbers as the numbering scheme.
GPIO.setmode(GPIO.BCM)

GPIO.setup(12,GPIO.OUT)
GPIO.setup(16,GPIO.OUT)
GPIO.setup(20,GPIO.OUT)
GPIO.setup(21,GPIO.OUT)

# Use GPIO12, 16, 20 and 21 for the buttons.

# Set GPIO numbers in the list: [12, 16, 20, 21] as input with pull-down resistor.

# Keep a list of the expected movements that the eBot should perform sequentially.
movement_list = []

done = False


while not done:
    print('in while')
    
    # Write your code here
    if GPIO.input(12) == GPIO.HIGH:
        print('in if 12')
        movement_list.append(12)
    elif GPIO.input(16) == GPIO.HIGH:
        print('in if 16')
        movement_list.append(16)
    elif GPIO.input(20) == GPIO.HIGH:
        print('in if 20')
        movement_list.append(20)
    elif GPIO.input(21) == GPIO.HIGH:
        movement_list.append(21)
        firebase.put('/', 'movement_list', movement_list) # n
        done = True
    else:
        pass
    
    '''
    We loop through the key (button name), value (gpio number) pair of the buttons
    dictionary and check whether the button at the corresponding GPIO is being
    pressed. When the OK button is pressed, we will exit the while loop and 
    write the list of movements (movement_list) to the database. Any other button
    press would be stored in the movement_list.

    Since there may be debouncing issue due to the mechanical nature of the buttons,
    we can address it by putting a short delay between each iteration after a key
    press has been detected.
    '''
# Write to database once the OK button is pressed
        
print(movement_list)
'''
robot = ThymioReal()

# Prompt user to enter speed and duration of movement

no_movements = True

while no_movements:
    x = firebase.get('/movement_list')
    if x != None:
        for i in x:   
            if i == 12:
                robot.wheels(100,100)
                robot.sleep(1)               
            elif i == 16:
                robot.wheels(-100,100)
                robot.sleep(1)
            elif i == 20:
                robot.wheels(100,-100)
                robot.sleep(1)
            else:
                robot.wheels(0,0)

        no_movements = False
    else:
        sleep(0.5)
        
    # Check the value of movement_list in the database at an interval of 0.5
    # seconds. Continue checking as long as the movement_list is not in the
    # database (ie. it is None). If movement_list is a valid list, the program
    # exits the while loop and controls the eBot to perform the movements
    # specified in the movement_list in sequential order. Each movement in the
    # list lasts exactly 1 second.
'''

    
    
