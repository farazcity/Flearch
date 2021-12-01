from flask import Flask,render_template,request,jsonify
from models import *

app=Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"]="postgres://postgres:postgres@localhost:5432/postgres"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False

db.init_app(app)

@app.route("/")
def index():
	flights=Flight.query.all()
	return render_template("index.html",flights=flights)

@app.route("/book",methods=["post"])
def book():
	name=request.form.get("name")
	try:
		flight_id=request.form.get("flight_id")
	except ValueError:
		return render_template("error.html")
	Passenger.add_passenger(name,flight_id)
	return render_template("success.html",name=name,flight_id=flight_id)

@app.route("/flights")
def flights():
	flights=Flight.query.all()
	return render_template("flights.html",flights=flights)

@app.route("/flight/<int:flight_id>")
def flight(flight_id):
	flight=Flight.query.get(flight_id)
	passengers=Passenger.query.filter_by(flight_id=flight_id)
	return render_template("flight.html",flight=flight,passengers=passengers)


