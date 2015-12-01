#!/usr/bin/python

#not really fast, but hey, it works!

def factorial(n):
	if n==1:
		return 1
	return n*factorial(n-1)
	
factlist = [1] + [factorial(i) for i in range(1,10)]		#list with factorials below 10

def digitfactorial(n):
	tot = 0
	for i in str(n):
		tot += factlist[int(i)]
	return tot

factlenlist = [0 for i in range(10**6)]

def factlength(n):	#returns length of a chain
	if factlenlist[n] > 0:
		return factlenlist[n]
	hadlist = [n]
	for i in range(60):
		new = digitfactorial(hadlist[i])
		if new in hadlist:
			for j in range(len(hadlist)):
				if hadlist[j] < 10**6:
					factlenlist[hadlist[j]] = i-j
			return i+1
		hadlist = hadlist + [new]
		
tot = 0
for i in range(10**6):
	if factlength(i) == 60:
		tot += 1
		
print tot