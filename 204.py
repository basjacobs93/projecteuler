#!/usr/bin/python

import time

start = time.clock()

h=[1]
 
bound=10**9

i2=i3=i5=i7=i11=i13=i17=i19=i23=i29=i31=i37=i41=i43=i47=i53=i59=i61=i67=i71=i73=i79=i83=i89=i97=0

counter = 0

while h[-1] <= bound:
	counter += 1
	while h[i2]*2<=h[-1]:
		i2+=1
	while h[i3]*3<=h[-1]:
		i3+=1
	while h[i5]*5<=h[-1]:
		i5+=1
	while h[i7]*7<=h[-1]:
		i7+=1
	while h[i11]*11<=h[-1]:
		i11+=1
	while h[i13]*13<=h[-1]:
		i13+=1
	while h[i17]*17<=h[-1]:
		i17+=1
	while h[i19]*19<=h[-1]:
		i19+=1
	while h[i23]*23<=h[-1]:
		i23+=1
	while h[i29]*29<=h[-1]:
		i29+=1
	while h[i31]*31<=h[-1]:
		i31+=1
	while h[i37]*37<=h[-1]:
		i37+=1
	while h[i41]*41<=h[-1]:
		i41+=1
	while h[i43]*43<=h[-1]:
		i43+=1
	while h[i47]*47<=h[-1]:
		i47+=1
	while h[i53]*53<=h[-1]:
		i53+=1
	while h[i59]*59<=h[-1]:
		i59+=1
	while h[i61]*61<=h[-1]:
		i61+=1
	while h[i67]*67<=h[-1]:
		i67+=1
	while h[i71]*71<=h[-1]:
		i71+=1
	while h[i73]*73<=h[-1]:
		i73+=1
	while h[i79]*79<=h[-1]:
		i79+=1
	while h[i83]*83<=h[-1]:
		i83+=1
	while h[i89]*89<=h[-1]:
		i89+=1
	while h[i97]*97<=h[-1]:
		i97+=1
	h.append(min(h[i2]*2,h[i3]*3,h[i5]*5,h[i7]*7,h[i11]*11,h[i13]*13,h[i17]*17,h[i19]*19,h[i23]*23,h[i29]*29,h[i31]*31,h[i37]*37,h[i41]*41,h[i43]*43,h[i47]*47,h[i53]*53,h[i59]*59,h[i61]*61,h[i67]*67,h[i71]*71,h[i73]*73,h[i79]*79,h[i83]*83,h[i89]*89,h[i97]*97))

print counter
print time.clock()-start