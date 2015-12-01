#!/usr/bin/python

import time

start = time.clock()

def totients(n):
	the_list = [[i,True] for i in xrange(1,n+1)]
	for i in the_list[1:]:
		if i[1] == True:
			p = i[0]
			i[0] = i[0]-1
			for j in the_list[2*p-1:n:p]:
				j[1] = False
				j[0] = int(j[0]*(1-1.0/p))
	return the_list

maxn = 0
maxtot = 2

a = totients(10**7)

print "Totient done:", time.clock()-start

for i in xrange(10**7):
	if a[i][1] == False:
		if sorted(str(a[i][0])) == sorted(str(i+1)):
			print i+1, a[i][0]
			if (i+1.0)/(a[i][0])<maxtot:
				maxn = i+1
				maxtot = (i+1.0)/a[i][0]
				print maxn, maxtot
			
print "Final:", maxn, maxtot
print "Time :", time.clock()-start