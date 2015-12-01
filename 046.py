import math, time

start = time.clock()

def is_prime(n):
  for i in range(2, int(math.sqrt(n))+1):
    if n%i == 0:
      return False
  return True
  
def is_sum(n):
  for i in range(2, n):
    if is_prime(i):
      for j in range(1, int(math.sqrt((n-i)/2)+1)):
        if n == i + 2*j**2:
          return True
  
for i in range(1, 10000, 2):
  if not is_prime(i):
    if not is_sum(i):
      print i
      break

print time.clock()-start