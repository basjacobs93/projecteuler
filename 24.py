import itertools

permlist = list(itertools.permutations([0,1,2,3,4,5,6,7,8,9]))
permlist.sort()
print permlist[999999]