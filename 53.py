import math, helpers, time, itertools

start = time.clock()

def nCr(n, r):
  return math.factorial(n)/(math.factorial(r)*math.factorial(n-r))

cnt = 0

for n in range(1, 101):
  for r in range(n):
    if nCr(n, r) > 1000000:
      cnt += 1
      
print cnt

print time.clock()-start