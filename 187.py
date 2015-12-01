#!/usr/bin/python

n=10**8

a = [0 for i in xrange(n)]

sum=0

for i in xrange(2,n):
	if a[i]==0:
		j=2
		while j*i<n:
			num=0
			if j%i==0:
				if (j/i)%i==0:
					num=3
				else:
					num=2
			else:
				num=1
			a[j*i]+=num
			j+=1
	elif a[i]==2:
		sum+=1
print sum