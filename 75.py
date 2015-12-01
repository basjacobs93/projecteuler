#!/usr/bin/python
import time
from fractions import gcd

start = time.clock()

upper_bound = 1500000
results = [0 for _ in xrange(0,upper_bound/2+1)]

total = 0

for r in xrange(1,upper_bound/2):
	for s in xrange(1,r):
		if r*(r+s)>upper_bound/2:
			break
		if gcd(r,s) == 1 and (r-s)%2 == 1:
			for k in xrange(1, upper_bound/2):
				if k*r*(r+s) > upper_bound/2:
					break
				results[k*r*(r+s)] += 1

total = 0
for i in results:
	if i == 1:
		total += 1

print "Result: {}".format(total)
print "Time  : {}".format(time.clock()-start)