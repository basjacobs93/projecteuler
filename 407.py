#!/usr/bin/python
import time

start = time.clock()

limit = 10**7

divs = [[] for _ in xrange(limit+1)]

for a in xrange(2,limit+1):
	k=a
	while k<limit:
		divs[k] += [a]
		k+=a
		
ans = [1 for _ in xrange(limit+1)]
tot = 0
for n in xrange(2,limit+1):
	for i in divs[n]:
		for j in divs[n-1]:
			p = i*j
			if p>limit:
				break
			if p>n:
				if ans[p]<n:
					ans[p]=n
	tot += ans[n]

print tot
print time.clock()-start
'''
For every a, the divisors n>a of a(a-1) satisfy
a^2=a (mod n)
'''