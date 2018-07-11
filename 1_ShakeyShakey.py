# Starting code to read the tilt sensor and increase score 

# import the RPi.GPIO library that lets you control the GPIO pins on the Raspberry Pi
import RPi.GPIO as GPIO

# Set up to use BCM numbering 
GPIO.setmode(GPIO.BCM)

# Set GPIO 4 as as input with pulldown resistor
GPIO.setup(4,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

#set the score to 0 at the start
score=0

# while True means do forever
while True:
    # if connection made increase score by 1 and display it
    if GPIO.input(4):
        score=score +1
        print("Your score is: " + str(score))
