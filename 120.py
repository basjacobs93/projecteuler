#!/usr/bin/python

tot = 0
for a in range(3,1001):
	rmax = 2
	for n in range(a):
		r = (2*n*a) % (a*a)
		if r>rmax:
			rmax = r
	print a, rmax
	tot += rmax
print tot