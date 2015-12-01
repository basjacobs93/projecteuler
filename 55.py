import math, time, helpers
start = time.clock()

def reverse(n):
  return int(str(n)[::-1])
  
def is_lychrel(n):
  for i in range(51):
    n += reverse(n)
    if helpers.is_palindromic(n):
      return False
  return True
  
cnt = 0
for i in range(1, 10000):
  if is_lychrel(i):
    print i
    cnt += 1

print 'count:', cnt

print time.clock()-start