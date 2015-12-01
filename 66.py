#!/usr/bin/python

#brute-force method
from decimal import *
import time

start = time.clock()

getcontext().prec = 100

def continued_fraction(n):
	a = Decimal(n).sqrt()
	continued_fraction = []
	num1 = den0 = 1
	den1 = num0 = 0
	while True:
		continued_fraction += [int(a)]
		helpnum = num1
		helpden = den1
		num1 = int(a)*num1+num0
		den1 = int(a)*den1+den0
		num0 = helpnum
		den0 = helpden
		if num0*num0-D*den0*den0==1 and den0!=0:
			return num0
		b = a - int(a)
		a = Decimal(1)/b

maxD = 0
maxr = 0

for D in range(2,1000):
	if int(D**0.5)**2 != D:
		a = continued_fraction(D)
		#print D, '\t', a
		if a > maxr:
			maxr = a
			maxD = D

print maxD, time.clock()-start