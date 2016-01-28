#!/usr/bin/python

'''
we calculate sum_{i=1}^n floor(n/i) * i^2
we can rewrite this as
( sum_{i=1}^sqrt(n) floor(n/i) * i^2 ) + ( sum_{i=sqrt(n)}^n floor(n/i) * i^2 )
where the first sum is calculated as usual, but the second sum can be rewritten as
sum_{j=1}^sqrt(n) (j sum_{i=n/(j+1)+1}^{n/j} i^2)
using sum_i=1^n i^2 = n(n+1)(2n+1)/6, the inner sum can be calculated quickly
'''

import time

start = time.clock()

bound = 10**15

a = int(bound**0.5)
b = bound/(a+1)

# original version
def gen(limit):
	sum = 0
	for n in xrange(1, limit + 1):
		sum += (bound/n)*n*n
	return sum

# k^2 + (k+1)^2 + ... + n^2
def squares(k,n):
	return (n*(n+1)*(2*n+1)-k*(k-1)*(2*k-1))/6

tot = gen(b)%10**9
tot += sum((squares(bound/(i+1)+1,bound/i)*i) for i in xrange(1,a+1))%10**9

print tot%10**9
print time.clock()-start