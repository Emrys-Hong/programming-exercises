import RPi.GPIO as GPIO
from time import sleep

# Use the BCM GPIO numbers as the numbering scheme
GPIO.setmode(GPIO.BCM)

# Use GPIO23 for LED 1, GPIO24 for LED 2 and GPIO18 for switch
led = [23, 24]
switch = 18

# Set the GPIO23 and GPIO24 as output.
GPIO.setup(led, GPIO.OUT)

# Set the GPIO18 as input with a pull-down resistor.
GPIO.setup(switch, GPIO.IN, GPIO.PUD_DOWN)

def blink(gpio_number, duration):
    GPIO.output(gpio_number, GPIO.HIGH)
    sleep(duration)
    GPIO.output(gpio_number, GPIO.LOW)
    sleep(duration)

while True:
    counter = 0
    if GPIO.input(switch) == GPIO.HIGH:
        while counter <= 10:
            if GPIO.input(switch) == GPIO.HIGH:
                blink(23, 1-counter/10)
                counter += 1
            else:
                break
    else:
        while counter <= 10:
            if GPIO.input(switch) == GPIO.LOW:
                blink(24, 1-counter/10)
                counter += 1
            else:
                break
   
