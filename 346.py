#!/usr/bin/python
import time

def StrongRepunits(limit = 50):
			sum = 1
			hadlist = set('1')
			for base in range(2, int(limit**0.5) + 1):
				 repunit = 1 + base + base**2
				 power = base**2
				 while repunit < limit:
					  if repunit not in hadlist:
					  		sum += repunit
							hadlist.add(repunit)
					  power *= base
					  repunit += power
			return sum

start = time.clock()			
print StrongRepunits(10**12)
print time.clock()-start