# Starting code to read the tilt sensor and increase score 
# Adding in slight pause to do de-bounce
# Adding in second tilt sensor
# Add timer to make it a game

# import the RPi.GPIO library that lets you control the GPIO pins on the Raspberry Pi
import RPi.GPIO as GPIO

# import sleep and time commands that lets you do a pause/wait and get the time in seconds
from time import sleep,time

# Set up to use BCM numbering 
GPIO.setmode(GPIO.BCM)

# Set GPIO 4 as as input with pulldown resistor
GPIO.setup(4,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
# Set GPIO 17 as a second input with pulldown resistor
GPIO.setup(17,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

# Set GPIO 4 as as input with pulldown resistor
score = 0 

# Get the current time as a marker
starttime = time()

# Set how long a turn is for (15 seconds)
duration = 15 

# Set the time the game ends
endtime = starttime + duration

# Give the player time to get ready
print("READY!")
sleep(1)
print("STEADY!")
sleep(1)
print("GO!!!!!!!")
sleep(0.5)

#While condition is where current time is less than start time + the duration (15 seconds)
while time() < endtime:
	
    # display the score and the amonut of time left 
    print("Your Score is: " + str(score) + " -  Time left: " +  str(endtime - time()))
    # if connection made increase score by 1
    if GPIO.input(4):
        score =score +1
        sleep(0.005)

        # stay in this while loop until GPIO17 is High or the time runs out
        while (not GPIO.input(17)) and (time() < endtime):
            print("Your Score is: " + str(score) + " -  Time left: " +  str(endtime - time()))
            
# Final score            
print("Your Final Score is: " + str(score))
