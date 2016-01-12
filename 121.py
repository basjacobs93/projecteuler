#!/usr/bin/python
from itertools import combinations as combs
from fractions import Fraction

maxi = 15
tot = 0
for i in range(maxi/2+1,maxi+1):
	#calculate probability of having exactly i right
	for j in combs(range(2, maxi+2), i):
		res = 1
		for k in range(2,maxi+2):
			if k in j:
				res *= Fraction(1,k)
			else:
				res *= Fraction(k-1,k)
		tot += res
print tot

#gives 9219406943/20922789888000
#so 2269