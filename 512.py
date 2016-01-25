#!/usr/bin/python

'''
We have f(p^k)=(p-1)p^(k-1) and f(p^k*q^l)=f(p^k)f(q^l).
'''

import math, time

start = time.clock()

bound = 5*10**8

sieve = [1 for _ in xrange(bound)]

for i in xrange(3,bound,2):
	if sieve[i]==1: #prime
		sieve[i]=(i-1) #f(p) = p-1
		#adjust multiples
		k = i+i
		while k<bound: 
			sieve[k]*=i-1
			k+=i
		#adjust powers
		p=i*i
		while p<bound:
			k = p
			while k<bound:
				sieve[k]*=i
				k+=p
			p *= i
		
print sum([sieve[i] for i in xrange(1,bound,2)])
print time.clock()-start