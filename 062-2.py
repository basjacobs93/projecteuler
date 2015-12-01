#!/usr/bin/python

import time, itertools

start = time.clock()

def generateCubes(n):
	dict = {}
	for i in range(1,n):
		a = ''.join(sorted(str(i**3))[::-1])
		if not a in dict.keys():
			dict[a] = [1, i**3]
		else:
			dict[a][0] += 1
			if dict[a][0] == 5:
				print "Found: {}".format(dict[a][1])
				break

generateCubes(10000)
	
print "Elapsed time: {}".format(time.clock()-start)