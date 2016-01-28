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
sleeptime=1
response={}
response['robot_check'] = False

GPIO.setmode(GPIO.BOARD)
GPIO.setup(StepPinForward, GPIO.OUT)
GPIO.setup(StepPinBackward, GPIO.OUT)
GPIO.setup(StepPinLeft, GPIO.OUT)
GPIO.setup(StepPinRight, GPIO.OUT)

def main():
    try:
        
        response['start'] = "Trying"
        GPIO.output(StepPinForward, GPIO.HIGH)
        forward = True
        time.sleep(0.02)
        GPIO.output(StepPinForward, GPIO.LOW)

        GPIO.output(StepPinBackward, GPIO.HIGH)
        backward = True
        time.sleep(0.02)
        GPIO.output(StepPinBackward, GPIO.LOW)
        
        GPIO.output(StepPinLeft, GPIO.HIGH)
        left = True
        time.sleep(0.02)
        GPIO.output(StepPinLeft, GPIO.LOW)

        GPIO.output(StepPinRight, GPIO.HIGH)
        right = True
        time.sleep(0.02)
        GPIO.output(StepPinRight, GPIO.LOW)     
        
        if forward and backward and left and right:
            response['robot_check'] = True
        
        GPIO.cleanup() 
        return response
    
    except ValueError:
        pass
        GPIO.cleanup()
        
print main()        
        
GPIO.cleanup()