#!/usr/bin/python
import math
f = math.factorial
lst = [0,2]
def s(n):
	if n<len(lst):
		return lst[n]
	t = 1
	for i in range(1,n+1):
		t += nCr(n,i)*(s(n-i)+1)
	lst.append(t/float(2**n-1))
	return lst[n]
		
def nCr(n,i):
	return f(n) / f(i) / f(n-i)
	
print s(32)