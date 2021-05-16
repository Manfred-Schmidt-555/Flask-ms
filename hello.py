from flask import Flask, render_template, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# create a Flask Instance
app = Flask(__name__)

# Secret Key!
app.config['SECRET_KEY'] = "mein super geheimes Passwort"

# Add Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'

# Initialize the Database
db = SQLAlchemy(app)

# Create Model
class Users(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(200), nullable=False)
	email = db.Column(db.String(120), nullable=False, unique=True)
	date_added = db.Column(db.DateTime, default=datetime.utcnow)

	#Create A String
	def __repr__(self):
		return '<Name %r>' % self.name


# create a UserForm Class
class UserForm(FlaskForm):
	name = StringField("Name", validators=[DataRequired()])
	email = StringField("Email", validators=[DataRequired()])
	submit = SubmitField("Submit")



# create a Form Class
class NamerForm(FlaskForm):
	name =StringField("Whats your name", validators=[DataRequired()])
	submit = SubmitField("Submit")


# Untersete "addd user"
@app.route('/user/add', methods=['GET', 'POST'])
def add_user():
	name = None
	form = UserForm()
	if form.validate_on_submit():
		user = Users.query.filter_by(email=form.email.data).first()
		if user is None:
			user = Users(name=form.name.data, email=form.email.data)
			db.session.add(user)
			db.session.commit()
		name = form.name.data
		form.name.date = ''
		form.email.data = ''
		flash("User Added Successfully")
	our_users = Users.query.order_by(Users.date_added)
	return render_template("add_user.html",
	form=form,
	name=name,
	our_users=our_users)

# create a rout decorator
@app.route('/')
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

# Create Name Page
@app.route('/name', methods=['GET', 'POST'])
def name():
	name = None
	form = NamerForm()
	# Validate Form
	if form.validate_on_submit():
		name = form.name.data
		form.name.data = ''
		flash("Form Submitted Successfully")
	return render_template("name.html",
		name = name,
		form = form)