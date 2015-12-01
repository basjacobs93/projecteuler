#!/usr/bin/python
import math, time

start = time.clock()
lst = []
def is_prime(n):
	if n==1:
		return False
	if n==2 or n==3:
		return True
	for i in range(2,int(math.sqrt(n))+1):
		if n%i == 0:
			return False
	return True

def is_harshad(n):
	return n % sum(int(i) for i in str(n)) == 0
	
def is_right_truncatable_harshad(n):
	if n<10:
		return True
	return is_harshad(n) and is_right_truncatable_harshad(int(str(n)[:-1]))

def is_strong_harshad(n):
	return is_prime(n/sum(int(i) for i in str(n)))

tot = 0

for i in xrange(11,10**6,2):
	if is_prime(i) and is_strong_harshad(int(str(i)[:-1])) and is_right_truncatable_harshad(int(str(i)[:-1])):
		print i
		tot += i
print tot
print time.clock()-start