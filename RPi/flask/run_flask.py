from flask import Flask, render_template, request
# from flask import *
app = Flask(__name__)
import sqlite3
from flask import g
import json

endTime = 0
userName = ""

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

@app.route('/saveTime', methods = ['GET', 'POST'])
def saveTime():
	if request.method == 'POST':
		global endTime
		endTime = request.json
		print endTime
	# else:
	# 	return render_template('saveTime.html')
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

# @app.route('/saveUser', methods=['GET','POST'])
# def saveUser():
# 	if request.method == 'POST':
# 		global userName
# 		userName = request.json
# 		print userName
# 	return render_template()

@app.route('/score', methods = ['GET','POST'])
def score():
	if request.method == 'POST':
		global userName
		userName = request.form['userName']
		userName = userName.upper()
		print userName
		global endTime
		to_insert = (userName,endTime,) # because this needs to be a tuple
		conn = sqlite3.connect('gameTimeDatabase.db')
		c = conn.cursor()
		c.execute("INSERT INTO times VALUES (?,?)", to_insert)
		conn.commit()
		allTimes = c.execute("SELECT * FROM times ORDER BY time")
		conn.commit()
		# c.execute("SELECT TOP 5")
		# print times
		# for row in times:
		# 	print row
		# timeString = "SELECT * FROM times ORDER BY time"
		# print timeString
		# pp.print(times)
		print allTimes

		# def dict_factory(cursor, row):
  #   		d = {}
  #   		for idx, col in enumerate(cursor.description):
  #       		d[col[0]] = row[idx]
  #   		return d

		# # con = sqlite3.connect(":memory:")
		# conn.row_factory = dict_factory
		# c.execute("select 1 as a")
		# print c.fetchone()["a"]

	return render_template('score.html', times = allTimes)


if __name__ == "__main__":
	conn = sqlite3.connect('gameTimeDatabase.db')
	c = conn.cursor()
	c.execute('''CREATE TABLE IF NOT EXISTS times (name, time)''')
	# c.execute("INSERT INTO times VALUES ('userName','endTime')") # ARE THESE QUOTES CORRECT? OR '''?
	conn.commit()

	app.debug = True
	app.run(host = '0.0.0.0')
