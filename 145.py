#!/usr/bin/python

import time

'''
if a0b works, then also a1b, a2b, ..., a4b work.
So count every a0b combination 5 times.

if a01b works, then also
a01b,a03b,a05b,a07b,a09b
a12b,a14b,a16b,a18b,
a21b,a23b,a25b,a27b,
a30b,a32b,a34b,a36b,
a41b,a43b,a45b,
a52b,a54b,
a61b,a63b,
a70b,a72b,
a81b,
a90b
so count every a01b combination 29 times


'''

def is_reversible(n):
	rev = int(str(n)[::-1])
	s = rev+n
	for i in str(s):
		if int(i)%2==0:
			return False
	return True
	
start = time.clock()

revs = [is_reversible(n) for n in xrange(10**9) if n%10!=0]
print sum(revs)
print time.clock()-start