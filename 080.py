#!/usr/bin/python
import math
from decimal import *
getcontext().prec = 120

def expand(n):
	if int(n**0.5)**2 != n:
		b = str(Decimal(n).sqrt())
		b = b.replace('.','')
		return sum([int(a) for a in str(b)[:100]])
	else:
		return 0

tot = 0
for i in range(1,101):
	tot += expand(i)
	
print tot