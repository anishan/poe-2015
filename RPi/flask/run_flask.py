# -*- coding: utf-8 -*-
import os, time
import multiprocessing
from flask import Flask, render_template, request
# from flask import *
app = Flask(__name__)
import sqlite3
from flask import g
import json
import RPi.GPIO as GPIO
import pygame
from pygame import mixer

# User information from web gui
endTime = 0
foul_time = 0
userName = ""
p = None
process1 = None

# Define GPIO pins 
arduino_reset_pin = 12
servo_control_pin = 21
pd1_pin = 6
pd2_pin = 13
pd3_pin = 19
pd4_pin = 26
# Initialize GPIO i/o
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(arduino_reset_pin, GPIO.OUT)
GPIO.setup(servo_control_pin, GPIO.OUT)
GPIO.setup(pd1_pin, GPIO.IN)
GPIO.setup(pd2_pin, GPIO.IN)
GPIO.setup(pd3_pin, GPIO.IN)
GPIO.setup(pd4_pin, GPIO.IN)

def game_state():
	pygame.init()
	while(1):
		#print 'Thread run'
		# Check for broken lazers
		p1 = GPIO.input(pd1_pin)
		p2 = GPIO.input(pd2_pin)
		p3 = GPIO.input(pd3_pin)
		p4 = GPIO.input(pd4_pin)
		pds = [p1, p2, p3, p4]
		pds = [0, 1, 0, 0]
		#print pds
		#global process1
		if 1 in pds:
			print pds
			# Play sad trombone sound
			#pds = [0, 0, 0, 0]
			print 'broken'
			#global process1
			#process1 = mutliprocessing.Process(target=play_sound, args = ())
			#process1.start
			#os.system('omxplayer -o local sad_trombone.wav')
			# Add time to the score
			#sounda = pygame.mixer.Sound('sad_trombone.wav')
			#sounda.play()
			mixer.music.load('sad_trombone.wav')
			mixer.music.play(0)
			time.sleep(4)
			global foul_time
			foul_time += 30
			#pds = [0,0,0,0]
		#else:
			#global process1
			#process1.terminate()

def play_sound():
	os.system('omxplayer -o local sad_trombone.wav')

@app.route('/')
def main():
	#pygame.init()
	#pygame.mixer.init()
	return render_template('index.html')

@app.route('/countDown')
def countDown():
	# Reset the Arduino for calibration
	GPIO.output(arduino_reset_pin, GPIO.LOW)
	GPIO.output(arduino_reset_pin, GPIO.HIGH)
	return render_template('countDown.html')

@app.route('/game')
def game():
	GPIO.output(servo_control_pin, GPIO.HIGH)
	print "game"
	global p
	p = multiprocessing.Process(target=game_state, args = ())
	p.start()
	return render_template('game.html')

@app.route('/saveTime', methods = ['GET', 'POST'])
def saveTime():
	print "save time"
	global p
	p.terminate()
	print request.method
	if request.method == 'POST':
		os.system('omxplayer -o local ta_da.wav')
		global endTime
		print 'first'
		print endTime
		endTime = request.json
		print 'second'
		print endTime
	return render_template('saveTime.html')

@app.route('/score', methods = ['GET','POST'])
def score():
	print 'score'
	if request.method == 'POST':
		global userName
		userName = request.form['userName']
		userName = userName.upper()
		print userName
		global endTime
		#global foul_time
		to_insert = (userName, endTime,) # because this needs to be a tuple
		conn = sqlite3.connect('gameTimeDatabase.db')
		c = conn.cursor()
		c.execute("INSERT INTO times VALUES (?,?)", to_insert)
		conn.commit()
		allTimes = c.execute("SELECT * FROM times ORDER BY time")
		conn.commit()

		#def from_sqlite_Row_to_dict(list_with_rows):
	    # '''Turn a list with sqlite3.Row objects into a dictionary'''
		 #   d = {} # the dictionary to be filled with the row data and to be returned

		  #  for i, row in enumerate(list_with_rows): # iterate throw the sqlite3.Row objects            
		   #     l = {} # for each Row use a separate list
		    #    l['name'] = str(row[0])
		     #   l['time'] = str(row[1])
		      #  d[i] = l   
		    #return d

		timeDict = from_sqlite_row_to_dict(allTimes)

	return render_template('score.html', times = timeDict)

def from_sqlite_row_to_dict(list_with_rows):
	d = {}
	for i, row in enumerate(list_with_rows):
		print row
		l = {}
		l['name'] = str(row[0])
		l['time'] = str(row[1])
		d[i] = l
	print d
	return d

if __name__ == "__main__":
	conn = sqlite3.connect('gameTimeDatabase.db')
	c = conn.cursor()
	c.execute('''CREATE TABLE IF NOT EXISTS times (name, time)''')
	conn.commit()

#	app.debug = True
	app.run(host = '0.0.0.0')
