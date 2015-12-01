import math, time

start = time.clock()

def is_pentagonal(n):
  x = (math.sqrt(24*n+1)+1)/6
  return int(x) == x

def is_hexagonal(n):
  x = (1+math.sqrt(1+8*n))/4
  return int(x) == x
  
for i in range(286, 100000):
  n = i*(i+1)/2
  if is_pentagonal(n) and is_hexagonal(n):
    print n
    print time.clock()-start
    quit()