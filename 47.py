import math, time

start = time.clock()

def is_prime(n):
  for i in range(2, int(math.sqrt(n))+1):
    if n%i == 0:
      return False
  return True

def primefactors(n, lst):
  if is_prime(n):
    isin = False
    for j in range(len(lst)):
      if lst[j][0] == n:
        lst[j][1] += 1
        isin = True
        break
    if not isin:
      lst.append([n,1])
    return lst
  for i in range(2, int(math.sqrt(n))+1):
    if n%i == 0:
      isin = False
      for j in range(len(lst)):
        if lst[j][0] == i:
          lst[j][1] += 1
          isin = True
          break
      if not isin:
        lst.append([i,1])
      if n/i == 1:
        return lst
      return primefactors(n/i, lst)

def is_disjoint(a, b):
  for i in a:
    if i in b:
      return False
  return True

def first_n(n):
  for i in range(1000000):
    lst = []
    for j in range(n):
      lst.append(primefactors(i+j, []))
    if all(len(x)==n for x in lst):
      disj = True
      for j in range(1, n):
        for k in range(j):
          if not is_disjoint(lst[j], lst[k]):
            disj = False
            break
      if disj == True:
        for j in range(n):
          print i+j, lst[j], len(lst[j])
        return

first_n(4)

print time.clock()-start