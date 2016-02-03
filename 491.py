#!/bin/bash

import itertools, time

start = time.clock()

'''
divisibility by 11: alternating sum needs to be divisible by 11
n						alternating sum
90908181727263635454	70-20=50
00112233445566778899	45-45=0
09091818272736364545	20-70=-50

Total digit sum is 90. Find 19<i,j<71 with i+j=90 and (i-j)%11==0. Gives: 
i	j	j-j
23 	67 	-44
34 	56 	-22
45 	45 	0
56 	34 	22
67 	23 	44

00112233445566778899

For each such a number we can swap around the numbers in every other position
e.g. 80809191727263635454 ~ 90908181727263635454
'''

def alternatingsum(n):
	return sum([int(n[i]) if i%2==0 else -int(n[i]) for i in range(len(n))])
	
def div11(n):
	return alternatingsum(n)%11==0

def sortstring(n):
	part1 = sorted(n[::2])
	part2 = sorted(n[1::2])
	return ''.join([part1[i/2] if i%2==0 else part2[i/2] for i in range(len(n))])

def countdoubles(n):
	counter = 0
	had1 = set([])
	had2 = set([])
	for i in n[::2]:
		if i in had1:
			counter += 1
		else:
			had1.add(i)
	for i in n[1::2]:
		if i in had2:
			counter += 1
		else:
			had2.add(i)
	return counter

def permutations(n):
	if n[0]=="0":
		if n[1]=="0": # two trailing zeros
			return 11851370496000/(2**countdoubles(n)) # 9*9!*10!, count all doubles
		else: # one trailing zero
			return 10534551552000/(2**countdoubles(n)) # 8*9!*10!, don't count double zero
	else: # no trailing zeros
		return 13168189440000/(2**countdoubles(n)) # 10!*10!, count all doubles
		
# contains all sorted numbers divisible by 11
anslist = set([])

for p in itertools.combinations("00112233445566778899",10):
	part1=''.join(p)
	part2 = ["0","0","1","1","2","2","3","3","4","4","5","5","6","6","7","7","8","8","9","9"]
	for i in part1:
		part2.remove(i)
	part2 = ''.join(part2)
	# merge together
	n = ''.join([part1[i/2] if i%2==0 else part2[i/2] for i in range(20)])
	if div11(n):
		anslist.add(sortstring(n))

print len(anslist)
print time.clock()-start

ans = 0
for i in anslist:
	ans += permutations(i)
	
print ans
print time.clock()-start
# for the answers, we need to count permutations
# total is 10! * 10!, but we need to check for doubles

