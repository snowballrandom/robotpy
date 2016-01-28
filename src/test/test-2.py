#!/usr/bin/python

import sys
import time
import RPi.GPIO as GPIO

# Use BCM GPIO references
# instead of physical pin numbers
#GPIO.setmode(GPIO.BCM)
mode=GPIO.getmode()
print " mode ="+str(mode)
GPIO.cleanup()

# Define GPIO signals to use
# Physical pins 11,15,16,18
# GPIO17,GPIO22,GPIO23,GPIO24

StepPinForward=16
StepPinBackward=18
StepPinLeft=15
StepPinRight=11
sleeptime=1

GPIO.setmode(GPIO.BOARD)
GPIO.setup(StepPinForward, GPIO.OUT)
GPIO.setup(StepPinBackward, GPIO.OUT)
GPIO.setup(StepPinLeft, GPIO.OUT)
GPIO.setup(StepPinRight, GPIO.OUT)
 
#total = len(sys.argv)
#cmdargs = str(sys.argv)
#print ("The total numbers of args passed to the script: %d " % total)
#print ("Args list: %s " % cmdargs)
# Pharsing args one by one 
#print ("Script name: %s" % str(sys.argv[0]))
#print ("First argument: %s" % str(sys.argv[1]))
#print ("Second argument: %s" % str(sys.argv[2]))
#print ("Third argument: %s" % str(sys.argv[3]))
#print ("Fourth argument: %s" % str(sys.argv[4]))

motor_forward = (sys.argv[1])
motor_reverse = (sys.argv[2])
motor_left = (sys.argv[3])
motor_right = (sys.argv[4])

slp = 1.5

def forward(x):
    GPIO.output(StepPinForward, GPIO.HIGH)
    print "forwarding running  motor "
    time.sleep(slp)
    GPIO.output(StepPinForward, GPIO.LOW)

def reverse(x):
    #GPIO.output(StepPinBackward, GPIO.HIGH)
    print "reversing running motor"
    #time.sleep(slp)
    #GPIO.output(StepPinBackward, GPIO.LOW)

def left(x):
    #GPIO.output(StepPinLeft, GPIO.HIGH)
    print "Motor Left"
    #time.sleep(slp)
    #GPIO.output(StepPinLeft, GPIO.LOW)
    
def right(x):
    #GPIO.output(StepPinRight, GPIO.HIGH)
    print "Motor Right"
    #time.sleep(slp)
    #GPIO.output(StepPinRight, GPIO.LOW)    

        

print "Forward Motor"
forward(motor_forward)
print "reverse motor"
reverse(motor_reverse)
print "Motor Left"
left(motor_left)
print "Motor Right"
right(motor_right)
print "Stopping motor"

