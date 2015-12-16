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

@app.route('/saveTime', methods = ['GET', 'POST'])
def saveTime():
	if request.method == 'POST':
		global endTime
		endTime = request.json
		print endTime
	return render_template('saveTime.html')

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

		def from_sqlite_Row_to_dict(list_with_rows):
	    # '''Turn a list with sqlite3.Row objects into a dictionary'''
		    d = {} # the dictionary to be filled with the row data and to be returned

		    for i, row in enumerate(list_with_rows): # iterate throw the sqlite3.Row objects            
		        l = {} # for each Row use a separate list
		        l['name'] = str(row[0])
		        l['time'] = str(row[1])
		        d[i] = l   
		    return d

		timeDict = from_sqlite_Row_to_dict(allTimes)

	return render_template('score.html', times = timeDict)


if __name__ == "__main__":
	conn = sqlite3.connect('gameTimeDatabase.db')
	c = conn.cursor()
	c.execute('''CREATE TABLE IF NOT EXISTS times (name, time)''')
	conn.commit()

	app.debug = True
	app.run(host = '0.0.0.0')
