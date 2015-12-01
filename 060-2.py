#!/usr/bin/python

import time
from helpers import is_prime
from itertools import combinations

start = time.clock()

def concat(lijst):
	for i, j in combinations(lijst, 2):
		if not is_prime(int(str(i)+str(j))) or not is_prime(int(str(j)+str(i))):
			return False
	return True

def primes(n):
	sieve = [True] * n
	for i in xrange(3,int(n**0.5)+1,2):
		if sieve[i]:
			sieve[i*i::2*i]=[False]*((n-i*i-1)/(2*i)+1)
	return [3]+[i for i in xrange(7,n,2) if sieve[i]]  #removed 2 and 5 manually

lst = primes(1000) #list with lots of primes
#need to split into 1 (mod 3) primes and 2 (mod 3) primes (if we concat two of them, they will become divisible by 3)

lst1mod3 = [3]
lst2mod3 = [3]

for i in lst[1:]:
	if i%3 == 1:
		lst1mod3.append(i)
	else:
		lst2mod3.append(i)
		
#print lst1mod3
#print lst2mod3

for a in combinations(lst1mod3, 5):
	if concat(a):
		print "FOUND " + str(a)
''' 
for a in combinations(lst1mod3, 4):
	if concat(a):
		print "FOUND " + str(a)
'''
print time.clock()-start
# around 51s with string concatination
# around 52s with integer concatination (with logarithms)