from flask import Flask,render_template,request,jsonify
from models import *

import threading,queue

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

@app.route("/min")
def min():
	return render_template("minimun0.html")

@app.route("/min/minimum")
def minimum():
	source=request.form.get("source")
	destination=request.form.get("destination")
	flights=Flight.query.all()


	class graph:

		def insert(self,airports):
			self.adj_list={}
			for a in airports:
				origin,destination=a.split(":")
				if origin not in self.adj_list:
					self.adj_list[origin]=[destination]
				else:
					self.adj_list[origin].append(destination)

		def display_adj_list(self):
			print(self.adj_list)

		def bfs(self,source):
			self.visited={}
			self.parent={}
			self.level={}
			self.traversal=[]
			for i in self.adj_list:
				self.visited[i]=False
				self.parent[i]=None
				self.level[i]=-1
			self.visited[source]=True
			self.level[source]=0
			q=queue.Queue()
			q.put(source)
			while not q.empty():
				u=q.get()
				self.traversal.append(u)
				for v in self.adj_list[u]:
					self.visited[v]=True
					self.parent[v]=u
					self.level[v]=self.level[u]+1
					q.put(v)

		def shortest_path(q):
			l=[]
			l.append(q)
			if self.parent(q)!=None:
				q=q.parent
			l.reverse()
			return(l)

		def bfs_data(self,data):
			def visited(self,data):
				return self.visited[data]
			def parent(self,data):
				return self.parent[data]
			def level(self,data):
				return self.level[data]
			def traversal(self):
				return self.traversal


	obj=graph()
	a=[]
	for i in flights:
		a.append(i.origin,i.destination)
	obj.insert(a)
	#obj.display_adj_list()
	obj.bfs("source")
	#print(obj.bfs_data.traversal())
	sp=obj.shortest_path("destination")
	
	return render_template("minimum.html",minimun=sp)








