#!/usr/bin/python

import sys
import time
import RPi.GPIO as GPIO

total = len(sys.argv)
cmdargs = str(sys.argv)    
motor_forward = float(sys.argv[1])
motor_reverse = float(sys.argv[2])
motor_left = float(sys.argv[3])
motor_right = float(sys.argv[4])

def main():
    print ("The total numbers of args passed to the script: %d " % total)
    try:        
        print "Forward Motor"
        forward(motor_forward)
        print "reverse motor"
        reverse(motor_reverse)
        print "Motor Left"
        left(motor_left)
        print "Motor Right"
        right(motor_right)
        print "Stopping motor"
    except ValueError:
        pass
        GPIO.cleanup()
GPIO.cleanup()