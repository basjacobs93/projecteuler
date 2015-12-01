import math

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def returndigs(n, digs):
  for i in range(0, int(math.log10(n))+1):
    ndig = n//(10**i) % 10
    if ndig in digs:
      digs.remove(ndig)
    else:
      return -1
  return digs
  
totlist = []

for i in range(1, 2000):
  for j in range(1, i):
    first = returndigs(j, [1, 2, 3, 4, 5, 6, 7, 8, 9])
    if first != -1:
      second = returndigs(i, first)
      if second != -1:
        third = returndigs(i*j, second)
        if third != -1 and len(third)==0:
          print j, 'x', i, '=', i*j
          if i*j not in totlist:
            totlist.append(i*j)

print totlist    
print 'total', sum(totlist)