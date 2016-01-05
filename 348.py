#!/usr/bin/python

def is_palindromic(n):
	if len(n)==0 or len(n)==1:
		return True
	elif n[0]==n[-1]:
		return is_palindromic(n[1:-1])
	else:
		return False

res = {}

for i in xrange(1,4*10**4):
	for j in xrange(1,2*10**3):
		a = i*i+j*j*j
		if a in res:
			res[a] += 1
		else:
			res[a] = 1
			
print "--"

for i in res:
	r = res[i]
	if r==4:
		if is_palindromic(str(i)):
			print i
			
'''
5229225+56200265+796767697+37088073+108909801
=
1004195061
'''