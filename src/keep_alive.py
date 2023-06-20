# create and deploy a flask webserver to keep bot alive for replit hosting

from flask import Flask
from threading import Thread
import random

app = Flask('')

@app.route('/')
def home():
	return 'Server Running'

def run():
	app.run(
		host='0.0.0.0',
		port=random.randint(2000,7000)
	)

def keep_alive():
	'''
	starts new thread that runs the function run
	'''
	t = Thread(target=run)
	t.start()