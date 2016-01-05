#!/usr/bin/python

results = [0 for _ in xrange(10**6+1)]
for u in xrange(1,10**6+1):
	v=u/3+1
	n = u*v
	while u*v<=10**6 and 3*v>u:
		if (u+v)%4==0:
			results[u*v] += 1
		v += 1
sum = 0
for n in results:
	if n == 10:
		sum += 1
		
print sum