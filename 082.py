#!/usr/bin/python

import time

start = time.clock()

matrix = []

# load in the matrix from the file
with open("082_matrix.txt", "r") as f:
	matrix+=[[int(i) for i in line.split(",")] for line in f]

size = len(matrix)
	
# dijkstra

def smallest(dist,visited): # finds the smallest unvisited node
	mina = 10**8
	mini = 0
	minj = 0
	for i in xrange(size):
		for j in xrange(size):
			if not visited[i][j]:
				if dist[i][j]<mina:
					mina = dist[i][j]
					mini = i
					minj = j
	return mini, minj

def neighbours(i,j,visited): # neighbours of i,j
	neighs = []
	if i+1<size and not visited[i+1][j]:
		neighs.append((i+1,j))
	if i>0 and not visited[i-1][j]:
		neighs.append((i-1,j))
	if j+1<size and not visited[i][j+1]:
		neighs.append((i,j+1))
	return neighs

def done(visited): # check if we visited all border points
	for i in xrange(size):
		if not visited[i][size-1]:
			return False
	return True
	
minsum = 10**8

# dijkstras loop
def dijkstra(k):
	dist = [[10**8 for i in xrange(size)] for i in xrange(size)]
	visited = [[False for i in xrange(size)] for i in xrange(size)]

	dist[k][0]=0 # distance of starting node is 0
	visited[k][0] = True
	current = (k,0)

	while not done(visited):
		for i,j in neighbours(current[0],current[1],visited):
			if dist[current[0]][current[1]]+matrix[current[0]][current[1]]<dist[i][j]:
				dist[i][j]=dist[current[0]][current[1]]+matrix[current[0]][current[1]]
		visited[current[0]][current[1]]=True
		current = smallest(dist,visited)
	return min([dist[i][size-1]+matrix[i][size-1] for i in xrange(size)])

mini = 10**8
for i in xrange(size): # perform dijkstra for every starting point
	a = dijkstra(i)
	if a<mini:
		mini=a
	print i, mini
#print min(dijkstra(i) for i in xrange(size))

print time.clock()-start