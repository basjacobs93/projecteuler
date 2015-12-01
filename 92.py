#!/usr/bin/python
import time

list = [0]*10**7
list[89] = 1
wronglist = [0]*10**7
wronglist[1] = 1

def square(n):
	return sum(int(a)*int(a) for a in str(n))
	
for i in xrange(1,len(list)):
	previous = [i]
	while i != 1:
		i = square(i)
		previous.append(i)
		if list[i] == 1:
			for j in previous:
				list[j] = 1
			break
		if wronglist[i] == 1:
			for j in previous:
				wronglist[j] = 1
			break
print sum(list)

#856929	10**6
#8581146 10**7