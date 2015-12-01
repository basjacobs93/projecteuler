import time

start = time.clock()

def is_pandigital(nums):
  lst = []
  for num in nums:
    for i in str(num):
      lst.append(int(i))
  if sorted(lst) == [1,2,3,4,5,6,7,8,9]:
    return int(''.join(map(str, lst)))
  else:
    return False

max = 0

for n in range(2, 10):
  for num in range(1, 10000):
    a = is_pandigital([a*num for a in range(1, n+1)])
    if a != False:
      if a>max:
        max = a
      print num, n, a

print 'max:', max

print time.clock()-start