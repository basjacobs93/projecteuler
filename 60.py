import time, math
from helpers import is_prime
from itertools import combinations

start = time.clock()
size = 10**5

def concat(i,j):
  if not is_prime(int(str(i)+str(j))) or not is_prime(int(str(j)+str(i))):
     return False
  return True

def primes(n):
  """ Returns  a list of primes < n """
  sieve = [True] * n
  for i in xrange(3,int(n**0.5)+1,2):
    if sieve[i]:
      sieve[i*i::2*i]=[False]*((n-i*i-1)/(2*i)+1)
  return [i for i in xrange(3,n,2) if sieve[i]]

lst = primes(size) #list with boolean values, True if prime (except for 2 and 5) and False otherwise

#need to split into 1 (mod 3) primes and 2 (mod 3) primes (if we concat two of them, they will become divisible by 3)

lst1mod3 = [3]
lst2mod3 = []

for i in lst:
  if i%3 == 1:
    lst1mod3.append(i)
  else:
    lst2mod3.append(i)
    
lst2mod3.remove(5) #gives trouble

def checklist(listname):
  for i in range(0,5):
    a = listname[i]
    for j in range(i,500):
      b = listname[j]
      if concat(a,b):
        for k in range(j,500):
          c = listname[k]
          if concat(a,c) and concat(b,c):
            for l in range(k, 800):
              d = listname[l]
              if concat(a,d) and concat(b,d) and concat(c,d):
                for m in range(l,len(listname)):
                  e = listname[m]
                  if concat(a,e) and concat(b,e) and concat(c,e) and concat(d,e):
                    print "FOUND: {} + {} + {} + {} + {} = {}".format(a,b,c,d,e,a+b+c+d+e) 

print "Lists made: " + str(time.clock()-start)

checklist(lst1mod3)
print "-second list-"
checklist(lst2mod3)

print "Done: " + str(time.clock()-start)