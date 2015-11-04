"""
Test File for Maze Prototypes
Edited: 11/3/15
"""

import os, time, sys
from pygame import mixer
import RPi.GPIO as GPIO


# Define GPIO and pins
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
laser_pin = 2
pd1_pin = 3

def sound_test(wav_file):
	os.system('omxplayer -o local ' + wav_file)

def laser_test():
	GPIO.setup(laser_pin, GPIO.OUT)
	GPIO.output(laser_pin, GPIO.HIGH)
	print 'Lasers On'
	time.sleep(20)

def diode_test():
	GPIO.setup(pd1_pin, GPIO.IN)
	while(1):
		pd1 = GPIO.input(pd1_pin)
		print pd1
		time.sleep(1)


#sound_test('sad_trombone.wav')
#laser_test()
diode_test()
