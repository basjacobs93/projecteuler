#!/usr/bin/python

import time
import numpy as np

start = time.clock()

def primesfrom2to(n):
	""" Input n>=6, Returns a array of primes, 2 <= p < n """
	sieve = np.ones(n/3 + (n%6==2), dtype=np.bool)
	sieve[0] = False
	for i in xrange(int(n**0.5)/3+1):
		if sieve[i]:
			k=3*i+1|1
			sieve[      ((k*k)/3)      ::2*k] = False
			sieve[(k*k+4*k-2*k*(i&1))/3::2*k] = False
	return np.r_[2,3,((3*np.nonzero(sieve)[0]+1)|1)]

primes = primesfrom2to(10**8)

for n in xrange(3,len(primes),2):
	p = primes[n-1]
	q = ((2*n*p) % (p**2))
	if q > 10**10:
		print n
		break

print time.clock()-start