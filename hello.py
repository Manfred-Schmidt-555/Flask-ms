from flask import Flask, render_template

# create a Flask Instance
app = Flask(__name__)

# create a rout decorator
@app.route('/')

def index():
	return "<h1> HelloWorld! </h1>"