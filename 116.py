#!/usr/bin/python

bound = 50

def f(n):
	if n<2:
		return 1
	res = 1
	while n!=1:
		res *= n
		n -= 1
	return res
	
facts = [f(n) for n in xrange(bound+1)]

def c(m,n):
	return facts[n+m]/(facts[n]*facts[m])

tot = 0

#red
for i in xrange(1,bound/2+1):
	tot += c(bound-2*i, i)

#green
for i in xrange(1,bound/3+1):
	tot += c(bound-3*i,i)

#blue
for i in xrange(1,bound/4+1):
	tot += c(bound-4*i,i)

print tot