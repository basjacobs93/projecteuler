import time, math

start = time.clock()

def is_prime(n):
  if n%2 == 0:
    return False
  for i in range(3, int(math.sqrt(n))+1, 2):
    if n%i == 0:
      return False
  return True
  
def replace_part(n, a):
  strn = str(n)
  for i in range(a, 10):
    yield int(strn.replace(str(a), str(i)))

for i in range(10000, 200000):
  if is_prime(i):
    for a in range(2):
      som = 0
      for j in replace_part(i, a):
        if is_prime(j):
          som += 1
      if som == 8:
        print i, a
        print time.clock() - start
        quit()