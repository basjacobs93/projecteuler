import math, time

start = time.clock()

def is_prime(n):
  for i in range(2, int(math.sqrt(n))+1):
    if n%i == 0:
      return False
  return True
    
def is_pandigital(num, n):
  for i in range(1, n+1):
    if not str(i) in str(num):
      return False
  return True

for i in xrange(1, 10**7, 2):
  j = 10**7-i
  if is_pandigital(j, len(str(j))) and is_prime(j):
    print j
    break

print time.clock()-start