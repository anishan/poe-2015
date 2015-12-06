import os, time
from flask import Flask, render_template
app = Flask(__name__)
import sqlite3
from flask import g
from pygame import mixer
import RPi.GPIO as GPIO

start_time = time.time()

# Define GPIO pins
arduino_reset_pin = 21
pd1_pin = 6
pd2_pin = 13
pd3_pin = 19
pd4_pin = 26
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(arduino_reset_pin, GPIO.OUT)
GPIO.setup(pd1_pin, GPIO.IN)
GPIO.setup(pd2_pin, GPIO.IN)
GPIO.setup(pd3_pin, GPIO.IN)
GPIO.setup(pd4_pin, GPIO.IN)

def game_state():
	# Check if lasers are broken
	# Check of stop button was pressed
	print 'game_state call'

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
	# Check for stop button
	# Check for 
	return render_template('game.html', python_function=game_state)

# @app.route('/sendTime', methods=['POST'])
# def sendTime():
# 	endTime = request.form['endTime']
# 	return endTime

@app.route('/saveTime')
def saveTime():
	#endTime = request.form['endTime']
	return render_template('saveTime.html')

@app.route('/saveUser', methods=['POST'])
def saveUser():
	userName = request.form['userName']
	return userName

@app.route('/score')
def score():
	cursor = gameTimeDatabase.execute('SELECT name,time FROM times')
	return render_template('score.html', items = cursor.fetchall())


if __name__ == "__main__":
	conn = sqlite3.connect('gameTimeDatabase.db')
	c = conn.cursor()
	c.execute('''CREATE TABLE IF NOT EXISTS times (name, time)''')
	c.execute("INSERT INTO times VALUES ('userName','endTime')")
	conn.commit()

	app.run(host='0.0.0.0')
