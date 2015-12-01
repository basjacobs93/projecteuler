#!/usr/bin/python

#first approach - takes ages

import itertools, math

def is_thirdpower(n):
	if n%5 == 0 and n%125 != 0:
		return False
	root = n**(1/3.0)
	return int(root+0.5)**3 == n

for i in xrange(1000,10000):
	if i%100 == 0:
		print i
	else:
		num = str(i*i*i)		#generate cube
		tot = [int(num)]
		for perm in itertools.permutations(num):		#this can (and should) be done more efficiently
			if perm[0] != '0':
				intperm = int(''.join(perm))
				if is_thirdpower(intperm):
					if not intperm in tot:
						tot = [intperm] + tot
						#print tot
					if len(tot) == 5:
						break
		if len(tot) == 4:
			print "Number found: {}".format(num)