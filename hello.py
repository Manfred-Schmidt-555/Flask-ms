from flask import Flask, render_template

# create a Flask Instance
app = Flask(__name__)

# create a rout decorator
@app.route('/')

#def index():
#	return "<h1> HelloWorld! </h1>"

def index():
	return render_template("index.html")

# localhost:5000/user/Manfred
@app.route('/user/<name>')

def user(name):
	return	"<h1>Hello {}!!!</h1>".format(name) 