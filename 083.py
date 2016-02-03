#!/usr/bin/python

import time

start = time.clock()

matrix = []

# load in the matrix from the file
with open("083_matrix.txt", "r") as f:
	matrix+=[[int(i) for i in line.split(",")] for line in f]

size = len(matrix)
	
# dijkstra

# tentative distances
dist = [[10**8 for i in xrange(size)] for i in xrange(size)]
visited = [[False for i in xrange(size)] for i in xrange(size)]

dist[0][0]=0 # distance of starting node is 0
visited[0][0] = True
current = (0,0)

def smallest(): # finds the smallest unvisited node
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

def neighbours(i,j): # neighbours of i,j
	neighs = []
	if i+1<size and not visited[i+1][j]:
		neighs.append((i+1,j))
	if i>0 and not visited[i-1][j]:
		neighs.append((i-1,j))
	if j+1<size and not visited[i][j+1]:
		neighs.append((i,j+1))
	if j>0 and not visited[i][j-1]:
		neighs.append((i,j-1))
	return neighs
	
# dijkstras loop
while not visited[size-1][size-1]:
	for i,j in neighbours(current[0],current[1]):
		if dist[current[0]][current[1]]+matrix[current[0]][current[1]]<dist[i][j]:
			dist[i][j]=dist[current[0]][current[1]]+matrix[current[0]][current[1]]
	visited[current[0]][current[1]]=True
	current = smallest()

print dist[size-1][size-1]+matrix[size-1][size-1]
print time.clock()-start