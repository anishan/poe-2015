#!/usr/local/bin/python

"""
input_control.pi
Description: Main control of lazer maze and GPIO
Edited: 10/26/15
"""

### Setup ###
import RPi.GPIO as GPIO
from android_connection import *

# GPIO setup
GPIO.setmode(GPIO.BCM)
# Servos
GPIO.setup(4, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
# Photocells
GPIO.setup(24, GPIO.IN)
GPIO.setup(25, GPIO.IN)
GPIO.setup(8, GPIO.IN)
GPIO.setup(7, GPIO.IN)
# Lasers
GPIO.setup(10, GPIO.out)

### Control ###
# Main Loop
while(1):
	# Get Photocell input
	pc1 = GPIO.input(4)
	pc2 = GPIO.input(17)
	pc3 = GPIO.input(21)
	pc4 = GPIO.input(22)
	PC = [pc1, pc2, pc3, pc4]
	# Get Android input
		
	# Determine if a beam was broken
	for pc in PC:
		if pc == False:
			# Set off alarm
			print "Beam Broken"
	# Update Servo positions 
	
