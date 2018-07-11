import RPi.GPIO as GPIO
from time import sleep, time 
GPIO.setmode(GPIO.BCM)
GPIO.setup(4,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(17,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

score = 0 
starttime = time()
duration = 15
endtime = starttime + duration
print("READY!")
sleep(1)
print("STEADY!")
sleep(1)
print("GO!!!!!!!!")

print("Start Now")
while time() < endtime:
    print("Your Score is: " + str(score)+ " - Time left: " +  str(endtime - time()))
    if GPIO.input(4):
        score =score +1
        sleep(0.005)
        while (not GPIO.input(17)) and (time() < endtime):
            print("Your Score is: " + str(score)+ " - Time left: " +  str(endtime - time()))
           
            
print("Your score is: " + str(score))
