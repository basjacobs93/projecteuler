#!/usr/bin/python

import time, math

start = time.clock()

def is_square(apositiveint):
	if apositiveint==1:
		return True
	x = apositiveint // 2
	seen = set([x])
	while x * x != apositiveint:
		x = (x + (apositiveint // x)) // 2
		if x in seen: return False
		seen.add(x)
	return True

a1 = 1
a2 = 3

while a2<5*10**11:
	a3 = 6*a2-a1-2
	a1 = a2
	a2 = a3
	
print a2
print time.clock()