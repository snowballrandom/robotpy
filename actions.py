#!/usr/bin/python

import sys
import time
import RPi.GPIO as GPIO

# Define GPIO signals to use
# Physical pins 11,15,16,18
# GPIO17,GPIO22,GPIO23,GPIO24

StepPinForward=16
StepPinBackward=18
StepPinLeft=15
StepPinRight=11
action=sys.argv[1]
sleeptime=float(sys.argv[2])

GPIO.setmode(GPIO.BOARD)
GPIO.setup(StepPinForward, GPIO.OUT)
GPIO.setup(StepPinBackward, GPIO.OUT)
GPIO.setup(StepPinLeft, GPIO.OUT)
GPIO.setup(StepPinRight, GPIO.OUT)

def main():
    try:
        if action == "forward":
            if sleeptime > 0 and sleeptime < 10:
                GPIO.output(StepPinForward, GPIO.HIGH)
                time.sleep(sleeptime)
                GPIO.output(StepPinForward, GPIO.LOW)
        elif action == "backward":
            if sleeptime:
                GPIO.output(StepPinBackward, GPIO.HIGH)
                time.sleep(sleeptime)
                GPIO.output(StepPinBackward, GPIO.LOW)   
        elif action == "right":
            if sleeptime:
                GPIO.output(StepPinRight, GPIO.HIGH)
                time.sleep(sleeptime)
                GPIO.output(StepPinRight, GPIO.LOW)   
        elif action == "left":
            if sleeptime:
                GPIO.output(StepPinLeft, GPIO.HIGH)
                time.sleep(sleeptime)
                GPIO.output(StepPinLeft, GPIO.LOW)                                            
        else:
            return sleeptime
            
        GPIO.cleanup() 
        return sleeptime
    
    except ValueError:
        pass
        GPIO.cleanup()
        return 1
        
print main()        
        
GPIO.cleanup()