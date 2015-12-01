#!/usr/bin/python

import time

start = time.clock()

with open('p067_triangle.txt', 'r') as f:
	#oneliner for creating list with elements of text file as ints
	list = [[int(b) for b in a.strip().split()] for a in f.readlines()]

while len(list) > 1:
	list[-2] = [max(list[-1][i],list[-1][i+1])+list[-2][i] for i in range(len(list[-2]))]		#take the maximum of each 'small triangle' and that will become the new list
	list.pop()

print "Sum : {}".format(max(list[0]))
print "Time: {}".format(time.clock()-start)