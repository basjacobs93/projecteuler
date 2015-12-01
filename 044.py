import time, math

start = time.clock()

def is_pentagonal(n):
  x = (math.sqrt(24*n+1)+1)/6
  return int(x) == x
      
for i in range(1, 5000):
  a = i*(3*i-1)/2
  for j in range(1, i):
    b = j*(3*j-1)/2
    if is_pentagonal(a-b) and is_pentagonal(a+b):
      print j, '=', b, 'and', i, '=', a, 'd=', a-b
      print time.clock()-start
      quit()