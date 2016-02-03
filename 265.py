#!/usr/bin/python

n = 5

strs = set([]) # generate subsequences
for i in xrange(2**n):
	strs.add(bin(i)[2:].zfill(n))
	
tot = 0
seqs = set([]) # generate sequences
for i in xrange(2**(2**n-n-1),2**(2**n-n)): # sequence must start with n zeros, then a 1
	binary = bin(i)[2:].zfill(2**n)+"0"*(n-1)
	
	works = True
	for j in strs:
		#print j, binary, j in binary
		if j not in binary:
			works = False
			break
	if works:
		tot += int(binary[:-n+1],2)
		
print tot