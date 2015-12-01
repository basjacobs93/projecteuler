#!/usr/bin/python

import fractions

for i in range(2,30):
	a=i*223092870
	b=15499*(a-1)
	tot=94744
	for j in range(2,a):
		if fractions.gcd(a,j)==1:
			tot += 94744
			if tot>b:
				break
	if tot<b:
		print a