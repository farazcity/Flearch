import threading,queue


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
		print(l)

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
a=[("nyc:ist"),("ist:dub"),("lon:dub"),("nyc:dub"),("ist:nyc"),("ist:dub")]
obj.insert(a)
obj.display_adj_list()
obj.bfs("ist")
print(obj.bfs_data.traversal())
