#!/usr/bin/python

import time

start = time.clock()

'''
ijkl
for every ij, we find pairs kl that can come after it
'''

digits = 20

thelist = [[[-1 for _ in range(digits/2)]+[1] for _ in range(10)] for _ in range(10)]

def counter(i,j, n=1):
	tot = thelist[i][j][n]
	if tot==-1:
		tot=0
		for k,l in pairlist[(i,j)]:
			a = thelist[k][l][n+1]
			if a == -1:
				a = counter(k,l,n+1)
				thelist[k][l][n+1] = a
			tot += a
		thelist[i][j][n]=tot
	return tot	


pairlist = {}
for i in range(10):
	for j in range(10-i):
		pairlist[(i,j)] = []
		for k in range(10-i-j):
			for l in range(10-j-k):
				pairlist[(i,j)].append((k,l))

tot = 0
for i in range(1,10):
	for j in range(10-i):
		tot += counter(i,j)
print tot
print time.clock()-start