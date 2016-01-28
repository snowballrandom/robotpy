#!/usr/bin/python

# Import required libraries
import sys
import time
import RPi.GPIO as GPIO

# Use BCM GPIO references
# instead of physical pin numbers
#GPIO.setmode(GPIO.BCM)
mode=GPIO.getmode()
#print " mode ="+str(mode)
#GPIO.cleanup()

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

motor_forward = float(input("Enter a forward number :"))
motor_reverse = float(input("Enter a reverse number :"))
motor_left = float(input("Enter a left number :"))
motor_right = float(input("Enter a right number :"))

def forward(x):
    GPIO.output(StepPinForward, GPIO.HIGH)
    print "forwarding running  motor "
    time.sleep(x)
    GPIO.output(StepPinForward, GPIO.LOW)

def reverse(x):
    GPIO.output(StepPinBackward, GPIO.HIGH)
    print "reversing running motor"
    time.sleep(x)
    GPIO.output(StepPinBackward, GPIO.LOW)

def left(x):
    GPIO.output(StepPinLeft, GPIO.HIGH)
    print "Motor Left"
    time.sleep(x)
    GPIO.output(StepPinLeft, GPIO.LOW)
    
def right(x):
    GPIO.output(StepPinRight, GPIO.HIGH)
    print "Motor Right"
    time.sleep(x)
    GPIO.output(StepPinRight, GPIO.LOW)    

print "Forward Motor"
forward(motor_forward)
print "reverse motor"
reverse(motor_reverse)
print "Motor Left"
left(motor_left)
print "Motor Right"
right(motor_right)
print "Stopping motor"
GPIO.cleanup()