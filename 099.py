#!/usr/bin/python
from decimal import Decimal, Context
ctx = Context(prec=20)
maxresult = Decimal(0)
maxpair = 0,0
i=0
with open('/Users/Bas/Downloads/p099_base_exp.txt','r') as f:
	for line in f:
		i+=1
		a,b = map(int,line.split(','))
		c = Decimal(b)*Decimal(a).ln(ctx)
		if c>maxresult:
			maxpair = a,b
			maxline = i
			maxresult = c
print maxpair
print maxline