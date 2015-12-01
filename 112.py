#!/usr/bin/python
import time

def is_bouncy(n):
	a = str(n)
	x = 0
	for i in range(1,len(str(n))):
		d = int(a[i])
		e = int(a[i-1])
		if d>e:
			if x==-1:
				return True
			x=1
		elif d<e:
			if x==1:
				return True
			x=-1
	return False
	
start = time.clock()

tot=0.0
for i in xrange(100,10**8):
	tot += is_bouncy(i)
	if tot/i==0.99:
		print i
		break
		
print time.clock()-start