import time
import flask
# from flask import Flask, render_template
app = Flask(__name__)
import sqlite3
from flask import g

start_time = time.time()


@app.route('/')
def main():
	return render_template('index.html')

# @app.route('/countDownPage1')
# def countDown1():
# 	return render_template('countDownPage1.html')

# @app.route('/countDownPage2')
# def countDown2():
# 	return render_template('countDownPage2.html')

# @app.route('/countDownPage3')
# def countDown3():
# 	return render_template('countDownPage3.html')

@app.route('/game')
def game():
	game_time = time.time() - start_time - 7
	game_time = round(game_time, 2)
	return render_template('game.html', game_time=game_time)

@app.route('/score')
def score():
	game_time = time.time() - start_time - 7
	return render_template('score.html', game_time=game_time)

if __name__ == "__main__":
	conn = sqlite3.connect('gameTimeDatabase.db')
	c = conn.cursor()
	c.execute('''CREATE TABLE times (name, time)''')


	app.run()
