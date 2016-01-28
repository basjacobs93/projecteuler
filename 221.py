#!/usr/bin/python

import sympy

ans = set([])

for p in xrange(10**5):
	divs = sympy.divisors(p*p+1)
	for i in divs:
		if i>p:
			break
		ans.add(2*p*p*p+p*p*((p*p+1)/i+i)+p)
		
print sorted(ans)[150000-1]