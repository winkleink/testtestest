# Starting code to read the tilt sensor and increase score 
# Adding in slight pause to do de-bounce
# Adding in second tilt sensor

# import the RPi.GPIO library that lets you control the GPIO pins on the Raspberry Pi
import RPi.GPIO as GPIO

# import sleep command that lets you do a pause/wait
from time import sleep

# Set up to use BCM numbering 
GPIO.setmode(GPIO.BCM)

# Set GPIO 4 as as input with pulldown resistor
GPIO.setup(4,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
# Set GPIO 4 as as input with pulldown resistor
GPIO.setup(17,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

# Set GPIO 4 as as input with pulldown resistor
score = 0 

while True:
    if GPIO.input(4):
        score =score +1
        sleep(0.005)
        print("Your score is: " + str(score))
        
        # stay in this while loop unti GPIO17 is High
        while not GPIO.input(17):
            sleep(0.005)
