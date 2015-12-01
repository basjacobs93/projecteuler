#!/usr/bin/python
import time

start = time.clock()

total = 0
for i in range(1,1000):
	found = False
	for j in range(1,1000):
		length = len(str(j**i))
		if length == i:
			found = True
			total += 1
		elif length > i:
			break
	if not found:
		break

print "Found: {}".format(total)
print "Time: {}".format(time.clock()-start)