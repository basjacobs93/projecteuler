import math, time

start = time.clock()

def primelist(n):
  primes = [2]
  for i in range(3, n**2, 2):
    for j in primes:
      if i%j == 0:
        break
      if j > math.sqrt(i):
        primes.append(i)
        break
    if len(primes)>n:
      return primes

def isprime(n):
  for i in range(2, int(math.sqrt(n)+1)):
    if n%i == 0:
      return False
  return True
  
def cumsum(lst):
  new = [0]
  for i in range(len(lst)):
    new.append(lst[i] + new[i])
  return new
  
def conseqsum(n):
  primes = primelist(n)
  
  cumul = cumsum(primes)
    
  maxj = 0
  pr = 0

  for i in range(int(n**1/4.0)):
    for j in range(1, int(n**1/4.0)):
      if cumul[i+j]-cumul[i] > n:
        break
      if isprime(cumul[i+j]-cumul[i]):
        if j > maxj:
          maxj = j
          pr = cumul[i+j]-cumul[i] 
      
  print maxj, pr

conseqsum(100000)
  
print time.clock()-start