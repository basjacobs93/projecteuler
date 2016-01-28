#!/usr/bin/python

'''
you cannot win if a xor 2a xor 3a == 0
this is only the case if a has no two adjacend 1's in its binary expansion
e.g.
 a		 2a		  3a
101 xor 1010 xor 1111 == 0
110 xor 1100 xor 10010 != 0

we write
works	cum. tot
0000	
0001	
----	2
0010	
----	3
0101	
0100
----	5
1000
1001
1010
----	8

a(n) = a(n-1) + a(n-2) with a(1)=2, a(2)=3
'''

f1 = 2
f2 = 3
counter = 1
while counter<30:
	tmp = f2
	f2 += f1
	f1 = tmp
	counter += 1
	
print f1