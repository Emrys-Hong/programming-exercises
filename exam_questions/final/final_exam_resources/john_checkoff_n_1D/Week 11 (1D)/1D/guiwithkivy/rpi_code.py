# -*- coding: utf-8 -*-
"""
Created on Wed Apr  4 17:57:19 2018

@author: jon_c
"""

from RPi import GPIO
from firebase import firebase

token = 'xbFBK0N1I9Id5ljHZAS9QitRXNdZzb0S3ZsAi1vH'
url = 'https://checkoff-6e917.firebaseio.com/'

firebase = firebase.FirebaseApplication(url,token)

GPIO.setmode(GPIO.BCM)
ledcolor={'yellow':23, 'red':24}
ledvalues = list(ledcolor.values())

GPIO.setup(ledvalues, GPIO.OUT)

def set_led(ledno, status):
    if(status == 'down'):
        GPIO.output(ledno, GPIO.HIGH)
    else:
        GPIO.output(ledno, GPIO.LOW)

	# you can use this to set the LED on or off

while True:
	# get firebase data and call setLED
    #check = firebase.get('/Check')
    yellow_status = firebase.get('/yellow_state') #check[0]
    red_status = firebase.get('/red_state') #check[1]
    print(yellow_status)
    set_led(ledcolor['yellow'], yellow_status)
    set_led(ledcolor['red'], red_status)
