#!/usr/bin/python
import fractions, time

start = time.clock()

bound = 4*10**7
length = 25

totients = [0,0]+[1 for _ in xrange(bound)]

tot = 0
i = 2
while i<bound:
	if totients[i]==1: # prime
		#multiples of i
		p = i
		while p<bound:
			totients[p]*=(i-1)
			p += i
		#multiples of powers of i
		p = i*i
		while p<bound:
			k = p
			while k<bound:
				totients[k]*=i
				k += p
			p *= i
		
		counter = 1
		x = i-1
		while x!=0:
			x = totients[x]
			counter += 1
			
		if counter==length:
			tot += i
			
	i += 1

print tot
print time.clock()-start