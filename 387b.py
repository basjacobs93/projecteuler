#!/usr/bin/python
import math, numpy, time

start = time.clock()
maxnum = 10**14

def primesfrom2to(n):
	""" Input n>=6, Returns a array of primes, 2 <= p < n """
	sieve = numpy.ones(n/3 + (n%6==2), dtype=numpy.bool)
	for i in xrange(1,int(n**0.5)/3+1):
		if sieve[i]:
			k=3*i+1|1
			sieve[       k*k/3     ::2*k] = False
			sieve[k*(k-2*(i&1)+4)/3::2*k] = False
	return numpy.r_[2,3,((3*numpy.nonzero(sieve)[0][1:]+1)|1)]

primelist = primesfrom2to(math.sqrt(maxnum))
print time.clock()-start
def is_prime(n):
	for i in primelist:
		if n == i:
			return True
		if n<math.sqrt(maxnum) and n<i:
			return False
		if n%i == 0:
			return False
	return True

lst = [a for a in range(1,10)]
t=0
for a in lst:
	if a>maxnum/10:
		break
	for j in range(10):
		if (10*a+j) % (sum(int(i) for i in str(a))+j) == 0:
			lst.append(10*a+j)
print time.clock()-start
som = 0
for i in lst:
	if is_prime(i/sum(int(j) for j in str(i))):
		for j in range(1,10,2):
			if is_prime(10*i+j):
				som += 10*i+j
print som
print time.clock()-start