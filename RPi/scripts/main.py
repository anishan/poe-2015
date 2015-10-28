#!/usr/local/bin/python

"""
main.py
Description: Main control of Lazer Maze and GPIO
Edited: 10/28/15
"""

### Setup ###
import RPi.GPIO as GPIO
import time

# Define pins
laserPin = 10
buttonPin = 23
servo1Pin = 4
servo2Pin = 17
servo3Pin = 21
servo4Pin = 22
pc1Pin = 24
pc2Pin = 25
pc3Pin = 8
pc4Pin = 7

# GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
# Servos
GPIO.setup(servo1Pin, GPIO.OUT)
GPIO.setup(servo2Pin, GPIO.OUT)
GPIO.setup(servo3Pin, GPIO.OUT)
GPIO.setup(servo4Pin, GPIO.OUT)
# Photocells
GPIO.setup(pc1Pin, GPIO.IN)
GPIO.setup(pc2Pin, GPIO.IN)
GPIO.setup(pc3Pin, GPIO.IN)
GPIO.setup(pc4Pin, GPIO.IN)
# Lasers
GPIO.setup(laserPin, GPIO.OUT)
# Finish button
GPIO.setup(buttonPin, GPIO.IN)


### Control ###
# Define the game functions
def game(level):
	# Record game start time
	startTime = time.time()
	# Turn on the lasers
	brokenLaser = False
	GPIO.output(laserPin, GPIO.HIGH)
	# Check for game actions
	while(brokenLaser == False and finish == False):
		# Update the timer
		currentTime = time.time()
		gameTime = currentTime - startTime
		# TODO: Send time to flask display
		# Check for finish button
		buttonState = GPIO.input(buttonPin)
		if buttonState == True:
			# TODO: Record finish time, score
			# TODO: End game flask meesage
			finish = True
		# Check for broken laser
		pc1 = GPIO.input(4)
		pc2 = GPIO.input(17)
		pc3 = GPIO.input(21)
		pc4 = GPIO.input(22)
		PC = [pc1, pc2, pc3, pc4]
		for pc in PC:
			if pc == False:
				brokenLaser = True
		if brokenLaser == True:
			# TODO: Record finish time, score
			# TODO: End game flask message
			pass

# Main Loop
def main():
	# Initialize level
	level = 1
	while(1):
		# Check flask input
		# TODO: Get flask states and input
		levelInput = False # TEMP: Getting rid of errors
		startGame = False # TEMP: Getting rid of errors		
		if levelInput == True:
			level = newLevel
		if startGame == True:
			game(level)

if __name__ == '__main__':
	main()
