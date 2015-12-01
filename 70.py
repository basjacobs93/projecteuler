#!/usr/bin/python

import fractions

def phi(n):
	if n%2 == 0:
		return 2*phi(n/2)
	number = 0
	for i in xrange(1,n):
		if fractions.gcd(i,n) == 1:
			number += 1
	return number
			
minn = 10**7
minphi = 1

minn = 0
minphi = 10**7

for i in xrange(3, 10**7):
	a = phi(i)
	if sorted(str(i)) == sorted(str(a)) and float(i)/a < minphi:
		minphi = float(i)/a
		minn = i
		print minphi, minn
	if i%1000 == 0:
		print i

print minphi, minn