#!/usr/bin/python

import time, math

start = time.clock()
bound = 10000000

#generate list with radicals, rad(n)=radicals[n]
radicals = [1 for _ in xrange(bound+1)]

for i in xrange(2,bound+1):
	if radicals[i]==1:
		radicals[i]=i
		for j in xrange(i+i, bound+1, i):
			radicals[j]*=i

print time.clock()-start

#for every n, finds max k s.t. rad(k)=n: maxradicals[n]=k
maxradicals = [0 for _ in xrange(bound+1)]

for i in xrange(bound+1):
	if i>maxradicals[radicals[i]]:
		maxradicals[radicals[i]]=i

#now, M(p,q,N) = maxradicals[p*q]

print time.clock()-start

#list with primes
primes = [1 for _ in xrange((bound+1)/2)]

for i in xrange(2,int(math.sqrt(len(primes)))):
	if primes[i]==1:
		for j in xrange(i+i,len(primes),i):
			primes[j]=0
			
primes = [i for i in xrange(2,(bound+1)/2) if primes[i]==1]

print time.clock()-start

tot = 0
for i in xrange(len(primes)):
	for j in xrange(i+1, len(primes)):
		p = primes[i]
		q = primes[j]
		if p*q<=bound:
			tot += maxradicals[p*q]
		else:
			break
print tot
print time.clock()-start