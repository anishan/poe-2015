import os, time, system
from flask import Flask, render_template
app = Flask(__name__)
import sqlite3
from flask import g
from pygame import mixer
import RPi.GPIO as GPIO

start_time = time.time()

# Define GPIO pins
arduino_reset_pin = 21
pdcontrol_pin = 5
pd1_pin = 6
pd2_pin = 13
pd3_pin = 19
pd4_pin = 26
GPIO.setup(arduino_reset_pin, GPIO.OUT)
GPIO.setup(pdcontrol_pin, GPIO.IN)
GPIO.setup(pd1_pin, GPIO.IN)
GPIO.setup(pd2_pin, GPIO.IN)
GPIO.setup(pd3_pin, GPIO.IN)
GPIO.setup(pd4_pin, GPIO.IN)

@app.route('/')
def main():
	# Reset arduino for calibration
	GPIO.output(arduino_reset_pin, 0)
	time.sleep(0.5)
	return render_template('index.html')

@app.route('/countDown')
def countDown():
	return render_template('countDown.html')

@app.route('/game')
def game():
	return render_template('game.html')

@app.route('/saveTime')
def saveTime():
	return render_template('saveTime.html')

@app.route('/score')
def score():
	return render_template('score.html')

@app.route('/sendTime', methods=['POST'])
def sendTime():
	text = request.form['endTime']
	return text

@app.route('/saveUser', methods=['POST'])
def saveUser():
	text = request.form['userName']
	return text
# I NEED TO FIGURE OUT HOW TO GET THESE VALUES INTO gameTimeDatabase.db

if __name__ == "__main__":
	conn = sqlite3.connect('gameTimeDatabase.db')
	c = conn.cursor()
	c.execute('''CREATE TABLE IF NOT EXISTS times (name, time)''')

	app.run(host='0.0.0.0')