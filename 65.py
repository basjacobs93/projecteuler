#!/usr/bin/python

import time

start = time.clock()

num1 = den0 = 1
den1 = num0 = 0

for i in range(100):
	if i == 0:
		a = 2
	elif i%3 != 2:
		a = 1
	else:
		a = 2*(i/3+1)
	helpnum = num1
	helpden = den1
	num1 = a*num1+num0
	den1 = a*den1+den0
	num0 = helpnum
	den0 = helpden

def sum(a):
	sum = 0
	for i in str(a):
		sum += int(i)
	return sum
	
print "Num: {}/{}".format(num1, den1)
print "Sum: {}".format(sum(num1))

print time.clock()-start