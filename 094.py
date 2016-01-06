#!/usr/bin/python

'''
a^2 = h^2 + ((a+1)/2)^2
4a^2 = h^2 + a^2 + 2a + 1
3a^2 = h^2 + 2a + 1
9a^2 = 3h^2 + 6a + 3
9a^2 - 6a + 1 = 3h^2 + 4
(3a^2-1)^2 = 3h^2 + 4
((3a^2-1)/2)^2 - 3(h/2)^2 = 1
x^2 - 3y^2 = 1
Pell equation

find solutions x,y
substitute back a=(2x+1)/3
other version: a=(2x-1)/3
whichever is an integer works
'''

x1=2
y1=1

xk=x1
yk=y1
som=0
for k in range(40):
	sol1 = (2*xk+1)/3
	sol2 = (2*xk-1)/3
	if sol1*3 == 2*xk+1:
		if sol1*3+1>1000000000:
			break
		som += sol1*3+1
	elif sol2*3 == 2*xk-1:
		if sol2*3+1>1000000000:
			break
		som += sol2*3+1
	xk1 = x1*xk+3*y1*yk
	yk = x1*yk+y1*xk
	xk = xk1
	#print xk, yk
print som #triangle 1,1,2 does not exist