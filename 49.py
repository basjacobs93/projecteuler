import math, time

start = time.clock()

def is_prime(n):
  for i in range(2, int(math.sqrt(n))+1):
    if n%i == 0:
      return False
  return True
  
def is_perm(a, b):
  if sorted(str(a)) == sorted(str(b)):
    return True
  return False
  
for i in range(10**3, 10**4):
  if is_prime(i) and is_prime(i+3330) and is_prime(i+6660):
    if is_perm(i, i+3330) and is_perm(i, i+6660):
      print i, i+3330, i+6660

print time.clock()-start