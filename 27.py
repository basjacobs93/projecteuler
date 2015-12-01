import math, itertools

primelist = [2]
for i in range(2,10000):
  divides = 0
  for x in primelist:
    if i%x == 0:
      divides = 1
      break
  if not divides:
    primelist.append(i)

def f(n, a, b):
  return n*n + a*n + b

maxcount = 0
maxa = 0
maxb = 0

for a in range(-1000, 1000):
  for b in primelist:
    if b > 999:
      break
    count = 0
    for n in itertools.count(0):
      if f(n, a, b) in primelist:
        count += 1
      else:
        break
    if count > maxcount:
      maxcount = count
      maxa = a
      maxb = b

print maxa, maxb, maxcount
for i in range(0, maxcount):
  print i, f(i, maxa, maxb)
print 'answer:', maxa*maxb