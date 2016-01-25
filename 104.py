#!/usr/bin/python
import time

start = time.clock()

f1 = 1
f2 = 1
f11 = 1
f22 = 1
i = 3
while i<10**12:
	temp = f1
	temp1 = f11
	f11 = f22
	f1 = f2
	f22 = temp1+f22
	if f22>10**12 & f11>10**12:
		f11 = f11/10**12
		f22 = f22/10**12
	f2 = (temp+f2)%10**9
	if ''.join(sorted(str(f2)))=="123456789" and ''.join(sorted(str(f22/(10**(len(str(f22))-9)))))=="123456789":
		print i
		break
	i += 1
	
print time.clock()-start