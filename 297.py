#!/usr/bin/python

import time

'''
found a relation: if s(n) is the sum upto number n and f(n) is biggest fibonacci number smaller than n:
	s(n) = s(f(n))+s(n-f(n))+n-f(n)
where s(f(n)) can be efficiently calculated (part 1)
'''

start = time.clock()

bound = 10**17

'''
part 1
'''
# generate f(n), s(f(n)) lists
fibons = [1]
sums = [1]

f1 = 1
f2 = 2
sum1 = 1
sum2 = 2

while f2<bound:
	temp = sum2
	sum2 += sum1+f1-1
	sum1 = temp
	fibons.append(f2)
	sums.append(sum1)
	temp = f2
	f2 += f1
	f1 = temp

'''
part 2
'''
# recursion
num = len(fibons)

def s(n):
	if n in fibons:
		return sums[fibons.index(n)]
	i = 0
	while i<num and fibons[i]<n:
		i += 1
	else:
		i -= 1
		return sums[i]+s(n-fibons[i])+n-fibons[i]

print s(bound-1)
print time.clock()-start