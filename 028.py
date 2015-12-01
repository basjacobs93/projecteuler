def diagonals(n): #creates list of diagonal elements of n by b spiral
  diaglist = [1]
  last = 1
  for i in range(2, n, 2):
    for j in range(4):
      last = last + i
      diaglist.append(last)
  return diaglist

print sum(diagonals(1001))