#!/usr/bin/python

import time
from decimal import *

start = time.clock()

getcontext().prec = 300

def continued_fraction(n):
	a = Decimal(n).sqrt()
	frst = int(a)
	continued_fraction = []
	for i in range(1,300):
		continued_fraction += [int(a)]
		b = a - int(a)
		a = Decimal(1)/b
		if int(a) == 2*frst:		#then we're done
			return i
	print "Error: no expansion for {} found".format(n)
	return 1

tot = 0
for j in range(2,10000):
	if not int(j**0.5+0.5)**2 == j:		#don't want any rational square roots
		if continued_fraction(j) % 2 == 1:	#if period length is odd
			tot += 1

print "Number of odd square roots: {}".format(tot)
print "Time                      : {}".format(time.clock()-start)