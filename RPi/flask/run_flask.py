from flask import Flask, render_template, request
# from flask import *
app = Flask(__name__)
import sqlite3
from flask import g
import json

endTime = 0

@app.route('/')
def main():
	return render_template('index.html')

@app.route('/countDown')
def countDown():
	return render_template('countDown.html')

@app.route('/game')
def game():
	return render_template('game.html')

# @app.route('/sendTime', methods=['POST'])
# def sendTime():
# 	endTime = request.form['endTime']
# 	return endTime

@app.route('/saveTime', methods = ['POST'])
def saveTime():
	time = request.json
	print time

	# jsdata = request.form['javascript_data']
	# finalTime = request.form.keys()
	# if request.method == 'POST':
	# 	finalTime = request.get_json()
	# # finalTime = str(request.method('finalTime'))
	# print finalTime
	# # ['finalTime']
	# finalTime = json.loads(finalTime)[0]
	# endTime = request.json
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

	app.debug = True
	app.run(host='0.0.0.0')
