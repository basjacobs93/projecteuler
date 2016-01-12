#!/usr/bin/python
from fractions import gcd

bound = 50

#right angle in bottom left corner: bound*bound
tot = bound*bound

#right angle in boundary point: bound*bound*2
tot += bound*bound*2

#right angle in interior point (x,y): comp(x,y)
def comp(x,y):
	res=0
	g = gcd(x, y)
	v=x/g
	u=y/g
	x1=x+u
	y1=y-v
	while x1>=0 and y1>=0 and x1<=bound and y1<=bound:
		res += 1
		x1 += u
		y1 -= v
	x1=x-u
	y1=y+v
	while x1>=0 and y1>=0 and x1<=bound and y1<=bound:
		res += 1
		x1 -= u
		y1 += v
	return res

for x in range(1,bound+1):
	for y in range(1,bound+1):
		c = comp(x,y)
		tot += c

print tot