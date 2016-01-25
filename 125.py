#!/usr/bin/python

import math
import time

start = time.clock()

def is_palindrome(st):
	if len(st)<2:
		return True
	if st[0]==st[-1]:
		return is_palindrome(st[1:-1])
	return False


bound = 10**8+1

ans = set([])
for n in xrange(1,int(math.sqrt(bound))+1):
	for k in xrange(1,bound):
		#p = sum of n^2+(n+1)^2+...+(n+k)^2
		p = (k+1)*(2*k*k+6*k*n+k+6*n*n)/6
		if p<bound:
			if is_palindrome(str(p)):
				ans.add(p)
		else:
			break

print "-----"
print sum(ans)
print time.clock()-start