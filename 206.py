#!/usr/bin/python
import math, time
start = time.clock()
for i in xrange(int(math.sqrt(10203040506070809)),int(math.sqrt(19293949596979899))):
	a = str(i*i)
	if a[0]=='1' and a[2]=='2' and a[4]=='3' and a[6]=='4' and a[8]=='5' and a[10]=='6' and a[12]=='7' and a[14]=='8' and a[16]=='9':
		print i*10
		print time.clock()-start
		break
