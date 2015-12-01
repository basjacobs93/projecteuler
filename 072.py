#!/usr/bin/python

def totients(n):
	the_list = [[i,True] for i in xrange(1,n+1)]
	for i in the_list[1:]:
		if i[1] == True:
			p = i[0]
			i[0] = i[0]-1
			for j in the_list[2*p-1:n:p]:
				j[1] = False
				j[0] = int(j[0]*(1-1.0/p))
	return [a[0] for a in the_list]
	
a = 0
for i in totients(10**6)[1:]:
	a += i

print a