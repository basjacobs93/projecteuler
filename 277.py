#!/usr/bin/python

import time

def a(n, st=""):
	if n==1:
		return st
	if n%3==0:
		return a(n/3,st+"D")
	elif n%3==1:
		return a((4*n+2)/3,st+"U")
	else:
		return a((2*n-1)/3,st+"d")
		
def a_inv(st,n):
	if st=="":
		return n
	s = st[-1]
	if s=="D":
		return a_inv(st[:-1],3*n)
	elif s=="U":
		p = 3*n-2
		if p%4==0:
			return a_inv(st[:-1],p/4)
		else:
			return 0
	else:
		p = 3*n+1
		if p%2==0:
			return a_inv(st[:-1],p/2)
		else:
			return 0

start = time.clock()		

st = "UDDDUdddDDUDDddDdDddDDUDDdUUDd"

for i in xrange(10**9):
	g = a_inv(st,i)
	if g:
		if g>10**15:
			print g
			break

print time.clock()-start