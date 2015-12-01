#!/usr/bin/python

array = []
'''reads the matrix'''
with open('/Users/Bas/Documents/ProjectEuler/081_matrix.txt','r') as f:
	for line in f:
		 array.append([int(a) for a in line.split(',')])
		
dist = [[10**10 for _ in range(80)] for _ in range(80)]
prev = [[None for _ in range(80)] for _ in range(80)]

def dijkstra():
	dist[0][0] = array[0][0]
	
	Q = [(i,j) for i in range(80) for j in range(80)]	#to do
	
	while len(Q)!=0:
		u = get_minimum(Q)
		Q.remove(u)
		if u == (79,79):	#we're done
			break
		for i in [(u[0]+1,u[1]),(u[0],u[1]+1)]:
			if i[0]<80 and i[1]<80:
				alt = dist[u[0]][u[1]] + array[i[0]][i[1]]
				if alt < dist[i[0]][i[1]]:
					dist[i[0]][i[1]] = alt
					prev[i[0]][i[1]] = u
	print dist[79][79]
	return prev
		
def get_minimum(Q):
	minelem = Q[0]
	for i in Q:
		if dist[i[0]][i[1]] < dist[minelem[0]][minelem[1]]:
			minelem = i
	return minelem
	
lst = dijkstra()
result = []
u = (79,79)
while lst[u[0]][u[1]]:
	result = [u] + result
	u = lst[u[0]][u[1]]
#print result #the route