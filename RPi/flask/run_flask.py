from flask import Flask, render_template
app = Flask(__name__)
import sqlite3
from flask import g

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

@app.route('/saveTime') #methods = ['POST']
def saveTime():
	endTime = request.form['endTime']
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
