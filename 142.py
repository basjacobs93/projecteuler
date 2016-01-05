#!/usr/bin/python

def is_square(apositiveint):
	if apositiveint==1:
		return True
	x = apositiveint // 2
	seen = set([x])
	while x * x != apositiveint:
		x = (x + (apositiveint // x)) // 2
		if x in seen: return False
		seen.add(x)
	return True

for i in xrange(1,10**4):
	l = i*i
	for j in xrange(1,i):
		p = j*j
		if is_square(l+p):
			for h in xrange(1,j):
				q = h*h
				if p%2 == q%2:
					if is_square(l+q):
						k = l+p+q
						if is_square(k):
							x = (k+l)/2
							y = (k-l)/2
							z = (p-q)/2
							print x, y, z
							
3713858 891458 88642