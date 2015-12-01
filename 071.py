#!/usr/bin/python

diff = 1
idiff = 0

for d in xrange(8,10**6):
	i = float(int(3*d/7.0-1))
	while i/d < 3.0/7:
		i = i+1.0
	i -= 1
	a = 3.0/7-i/d
	if a < diff:
		idiff = int(i)
		diff = a
		
print idiff, diff