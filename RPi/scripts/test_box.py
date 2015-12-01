"""
Test File for Maze Prototypes
Edited: 11/3/15
"""
import os, time, system
from pygame import mixer
import RPi.GPIO as GPIO

#Define GPIO and pins
GPIO.setmode(GPIO.BCM)
laser_pin = 2
pd1_pin = 2
GPIO.setup(pd1_pin, GPIO.IN)

def sound_test(wav_file):
	os.system('omxplayer -o local '+ wav_file)

def diode_test():
	pd1 = GPIO.input(pd1_pin)
	return pd1

def game_test():
	diode1 = diode_test()
	while diode1 == 1:
		diode1 = diosde_test()
		print diode1
	sound_test('sad_trombone.wav')

game_test()
