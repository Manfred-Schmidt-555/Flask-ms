from flask import Flask, render_template

# create a Flask Instance
app = Flask(__name__)

# create a rout decorator
@app.route('/')

#def index():
#	return "<h1> HelloWorld! </h1>"

def index(): 
	first_name = "Manfred"
	stuff = "This is<strong> Bold </strong>"

	# "list"  einführen
	favorite_pizza = ["pepperoni", "tomato", "mushroom", 42]

	# ein Kommentar
	# so, hier verweise ich auf index.html in templates
	# und kann Werte zuweisen "first_namw, stuff"
	# in der *.html Daei kann ich "Filter" setzen: "capitalize, lower,…""
	return render_template("index.html",  
		first_name=first_name,
		stuff=stuff, 
		favorite_pizza = favorite_pizza,) #dies wird in der index.html verwendet

# localhost:5000/user/Manfred
@app.route('/user/<name>')

def user(name):
	return render_template("user.html", user_name=name)

# Create Custom Error Pages

# Invalid URL
@app.errorhandler(404)  #eine Flaks Funktion
def page_not_found(e):
	return render_template("404.html"), 404

	# Internal Server Error
@app.errorhandler(500)  #eine Flaks Funktion
def page_not_found(e):
	return render_template("500.html"), 500