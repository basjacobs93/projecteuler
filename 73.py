#!/usr/bin/python

import fractions, time

start = time.clock()

def totient(n):
	tot = 0
	for i in range(int(n/3.0),int(n/2.0+1)):
		if fractions.gcd(n,i) == 1 and 1.0/3 < float(i)/n < 1.0/2:
			tot += 1
	return tot
	
tot = 0
for i in range(1, 9):
	tot += totient(i)
	
print tot
print time.clock()-start