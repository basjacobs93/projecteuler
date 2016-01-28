import time
import numpy as np

def primesfrom2to(n):
	sieve = np.ones(n/3 + (n%6==2), dtype=np.bool)
	sieve[0] = False
	for i in xrange(int(n**0.5)/3+1):
		if sieve[i]:
			k=3*i+1|1
			sieve[      ((k*k)/3)      ::2*k] = False
			sieve[(k*k+4*k-2*k*(i&1))/3::2*k] = False
	return np.r_[2,3,((3*np.nonzero(sieve)[0]+1)|1)]

# since (p-1)! + (p-2)! + (p-3)! + (p-4)! + (p-5)! = 9 (p-5)! (mod p)
# 24 (p-5)! = -1 (mod p), so need inverse of 24 modulo p
# can also invert 8 and multiply result with 3 to get answer
# since 2^-1 = (p+1)/2 (mod p), we need to cube (p+1)/2 mod p for result
def S(p):
	a = (p+1)/2
	b = (a*a)%p
	return (-3*((b*a)%p))%p

start = time.clock()
tot=0
maxi=10**8
primes = primesfrom2to(maxi)

print time.clock()-start
print len(primes[2:])
for i in xrange(len(primes[2:])):
	tot+=S(primes[2+i])
			
print tot
print time.clock()-start