#!/usr/bin/python

def mod(n):
	a = 1
	b = 1
	c = 3
	skip = False
	while ((a,b,c) != (1,1,1)) and (not skip):
		temp = (a+b+c)%n
		a = b
		b = c
		c = temp
		if c==0:
			skip = True
	if skip:
		return True #does divide a term
	else:
		return False #does not divide a term
counter = 0
for i in xrange(1,10**4,2):
	if not mod(i):
		counter += 1
	if counter==124:
		print i
		break