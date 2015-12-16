import os, time
from flask import Flask, render_template
app = Flask(__name__)
import sqlite3
from flask import g
from pygame import mixer
import RPi.GPIO as GPIO

endTime = 0

start_time = time.time()
global added_time
global n_broken

# Define GPIO pins
arduino_reset_pin = 21
pd1_pin = 6
pd2_pin = 13
pd3_pin = 19
pd4_pin = 26
stop_button_pin = 12
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(arduino_reset_pin, GPIO.OUT)
GPIO.setup(pd1_pin, GPIO.IN)
GPIO.setup(pd2_pin, GPIO.IN)
GPIO.setup(pd3_pin, GPIO.IN)
GPIO.setup(pd4_pin, GPIO.IN)
GPIO.setup(stop_button_pin, GPIO.IN)

def game_state():
	# Check if lasers are broken
	p1 = GPIO.input(pd1_pin)
	p2 = GPIO.input(pd2_pin)
	p3 = GPIO.input(pd3_pin)
	p4 = GPIO.input(pd4_pin)
	pds = [p1, p2, p3, p4]
	if 1 in pds:
		# Play trombone sound
		os.system('omxplayer -o local sad_trombone.wav')
		# Add time to the score (currently added at the end)
		added_time += 30
		n_broken += 1
		print 'Laser Broken'
	# Check if the stop button was pressed
	if GPIO.input(stop_button_pin) == 1:
		os.system('omxplayer -o local ta_da.wav')

def end_game():
	os.system('omxplayer -o local ta_da.wav')			

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
	return render_template('game.html', python_function=game_state)

# @app.route('/sendTime', methods=['POST'])
# def sendTime():
# 	endTime = request.form['endTime']
# 	return endTime

@app.route('/saveTime', methods = ['POST'])
def saveTime():
	global endTime
	endTime = request.json + added_time
	return render_template('saveTime.html')

# @app.route('/saveUser', methods=['POST'])
# def saveUser():
# 	userName = request.form['userName']
# 	return userName

@app.route('/score')
def score():
	userName = request.form['userName']
	# userName = "isfodjkl"
	global endTime
	to_insert = (userName,endTime,) # because this needs to be a tuple
	# cursor = gameTimeDatabase.execute('SELECT name,time FROM times')
	conn = sqlite3.connect('gameTimeDatabase.db')
	c = conn.cursor()
	c.execute("INSERT INTO times VALUES (?,?)", to_insert)
	c.execute("SELECT * FROM times ORDER BY time")
	c.execute("SELECT TOP 5")
	conn.commit()

	return render_template('score.html', items = cursor.fetchall())


if __name__ == "__main__":
	conn = sqlite3.connect('gameTimeDatabase.db')
	c = conn.cursor()
	c.execute('''CREATE TABLE IF NOT EXISTS times (name, time)''')
	# c.execute("INSERT INTO times VALUES ('userName','endTime')") # ARE THESE QUOTES CORRECT? OR '''?
	conn.commit()

	app.run(host='0.0.0.0')
