numlist = []
for a in range(2, 101):
  for b in range(2, 101):
    c = a**b
    if c not in numlist:
      numlist.append(a**b)
      
print len(numlist)