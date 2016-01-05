#!/usr/bin/python
'''
through examining the outcomes, I found that the
number of entries in row n that are not divisible by 7
the product of (coefficients+1) when n is written in
base 7
'''
steps = [1,1,1,1,1,1,1,1,1,1,1,1,1]

def updatesteps(i=0):
	steps[i] += 1
	if steps[i]%8==0:
		steps[i]=1
		updatesteps(i+1)

def calccounter():
	prod = 1
	for i in steps:
		prod *= i
	return prod

tot = 0
counter = 1

for i in xrange(10**9):
	counter = calccounter()
	#print i, counter
	updatesteps()
	tot += counter


print tot