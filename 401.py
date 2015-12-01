#!/usr/bin/python

import time

def sigma(n):
	tot = 0
	for i in xrange(1,int(n**0.5)+1):
		if n%i==0:
			if i*i==n:
				tot += n
			else:
				tot += i**2+(n/i)**2
			tot = tot%(10**9)
	return tot
	
start = time.clock()

tot = 1
for i in xrange(2,10**15):
	tot += sigma(i)
	tot = tot%(10**9)
print tot

print time.clock()-start