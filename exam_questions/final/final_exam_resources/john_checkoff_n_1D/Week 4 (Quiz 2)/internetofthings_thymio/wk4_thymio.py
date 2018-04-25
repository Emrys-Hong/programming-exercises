from pythymiodw import *
from time import sleep
from firebase import firebase

url = 'https://dw-1d-b57fd.firebaseio.com/' # URL to Firebase database
token = 'njrn9ydmOZK8q3z7kTycgl1t5VIqAhAcRua8aj92' # unique token used for authentication

# Create a firebase object by specifying the URL of the database and its secret token.
# The firebase object has functions put and get, that allows user to put data onto 
# the database and also retrieve data from the database.
firebase = firebase.FirebaseApplication(url, token)

robot = ThymioReal() # create an eBot object

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
        firebase.put('/', 'movement_list', []) 

        no_movements = False
    else:
        sleep(0.5)
    # Check the value of movement_list in the database at an interval of 0.5
    # seconds. Continue checking as long as the movement_list is not in the
    # database (ie. it is None). If movement_list is a valid list, the program
    # exits the while loop and controls the eBot to perform the movements
    # specified in the movement_list in sequential order. Each movement in the
    # list lasts exactly 1 second.

    # Write your code here


# Write the code to control the eBot here

# 'up' movement => robot.wheels(100, 100)
# 'left' movement => robot.wheels(-100, 100)
# 'right' movement => robot.wheels(100, -100)

