#!/usr/bin/python

def pentagonal(n):
	if n%2==1:
		a=n/2+1
	else:
		a=-n/2
	return a*(3*a-1)/2 
	
def sg(n):
	if n%4==1 or n%4==2:
		return 1
	else:
		return -1

lst = [1,1]

def partition(n):
	if n<0:
		return 0
	elif n == 0:
		return 1
	else:
		tot = 0
		k = 1
		p = 1
		while p<=n:
			tot = tot + sg(k)*lst[n-p]
			k += 1
			p = pentagonal(k)
		return tot

i=2
while True:
	a = partition(i)%1000000
	lst.append(a)
	if a == 0:
		print i
		break
	i+=1