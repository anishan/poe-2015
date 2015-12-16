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

		def from_sqlite_Row_to_dict(list_with_rows):
	    # '''Turn a list with sqlite3.Row objects into a dictionary'''
		    d = {} # the dictionary to be filled with the row data and to be returned

		    for i, row in enumerate(list_with_rows): # iterate throw the sqlite3.Row objects            
		        l = {} # for each Row use a separate list
		        l['name'] = str(row[0])
		        l['time'] = str(row[1])
		        # for col in range(0, len(row)): # copy over the row date (ie. column data) to a list
		        #     l.append(row[col])
		        d[i] = l
		        # d.append(l) # add the list to the dictionary   
		    return d

		timeDict = from_sqlite_Row_to_dict(allTimes)
		# print timeDict

		# def dict_factory(cursor, row):
  #   		d = {}
  #   		for idx, col in enumerate(cursor.description):
  #       		d[col[0]] = row[idx]
  #   		return d

		# # con = sqlite3.connect(":memory:")
		# conn.row_factory = dict_factory
		# c.execute("select 1 as a")
		# print c.fetchone()["a"]

	return render_template('score.html', times = timeDict)


if __name__ == "__main__":
	conn = sqlite3.connect('gameTimeDatabase.db')
	c = conn.cursor()
	c.execute('''CREATE TABLE IF NOT EXISTS times (name, time)''')
	# c.execute("INSERT INTO times VALUES ('userName','endTime')") # ARE THESE QUOTES CORRECT? OR '''?
	conn.commit()

	app.debug = True
	app.run(host = '0.0.0.0')
