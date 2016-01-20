#!/usr/bin/python

from fractions import gcd
import time

start = time.clock()
bound = 120000

#generate list with radicals
radicals = [1 for _ in xrange(bound+1)]

for i in xrange(2,bound+1):
	if radicals[i]==1:
		radicals[i]=i
		for j in xrange(i+i, bound+1, i):
			radicals[j]*=i

tot = 0

for a in xrange(1,bound/2+1):
	for b in xrange(a+1,bound-a, 2-a%2):
		c=a+b
		if radicals[a]*radicals[b]*radicals[c]<c:
			if gcd(a,b)==1:
				tot += c
				print a

print tot
print time.clock()-start