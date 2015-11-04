"""
Test File for Maze Prototypes
Edited: 11/3/15
"""

import os, time, sys
from pygame import mixer


def sound_test(wav_file):
	os.system('omxplayer -o local ' + wav_file)

def laser_test():
	pass

def diode_test():
	pass


sound_test('sad_trombone.wav')
