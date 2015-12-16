"""
Test File for Maze Prototypes
Edited: 11/3/15
"""
import os, time
from pygame import mixer
import RPi.GPIO as GPIO

#Define GPIO and pins
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
pd1_pin = 6
GPIO.setup(pd1_pin, GPIO.IN)
pd2_pin = 13
GPIO.setup(pd2_pin, GPIO.IN)
pd3_pin = 19
GPIO.setup(pd3_pin, GPIO.IN)
pd4_pin = 26
GPIO.setup(pd4_pin, GPIO.OUT)
reset_pin = 21
GPIO.setup(reset_pin, GPIO.OUT)
servo_pin = 12
GPIO.setup(servo_pin, GPIO.OUT)

def sound_test(wav_file):
	os.system('omxplayer -o local '+ wav_file)

def diode_test():
	pd1 = GPIO.input(pd1_pin)
	return pd1

def game_test():
	#print GPIO.input(pd1_pin)
	#print GPIO.input(pd2_pin)
	#print GPIO.input(pd3_pin)
	#print GPIO.input(pd4_pin)
	#time.sleep(0.5)
	#GPIO.output(reset_pin, GPIO.LOW)
	#GPIO.output(reset_pin, GPIO.HIGH)
	#print "RESET"
	#GPIO.output(servo_pin, GPIO.LOW)
	#print 'Servo'
	#diode1 = diode_test()
	#while diode1 == 1:
		#diode1 = diosde_test()	
	#sound_test('sad_trombone.wav')
	

game_test()
