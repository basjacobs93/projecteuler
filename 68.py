#!/usr/bin/python

#16-digit string, so 10 should be in one of the outer places

import time, itertools

start = time.clock()

''' SOLUTION FOR EXAMPLE
def listsum(the_list):
	tot = 0
	for i in the_list:
		tot += i
	return tot
	
def printstring(list1, list2, list3):
	if list1[0] < list2[0] and list1[0] < list3[0]:
		lst = [list1, list2, list3]
	elif list2[0] < list1[0] and list2[0] < list3[0]:
		lst = [list2, list3, list1]
	else:
		lst = [list3, list1, list2]
	res = ''
	for i in lst:
		res += ''.join([str(a) for a in i])
	return res
	
list1 = [0,0,0]
list2 = [0,0,0]
list3 = [0,0,0]

maxstring = ""

for i in range(1,7):
	for j in range(1,7):
		if j!= i:
			for k in range(1,7):
				if k!= j and k!=i:
					list1[0] = i
					list1[1] = j
					list1[2] = k
					list2[1] = k
					list3[2] = j
					for l in range(1,7):
						if l!=k and l!=i and l!=j:
							list2[2] = l
							list3[1] = l
							available = [1,2,3,4,5,6]
							available.remove(i)
							available.remove(j)
							available.remove(k)
							available.remove(l)
							if listsum(list1)-listsum(list2[1:]) in available:
								available.remove(listsum(list1)-listsum(list2[1:]))
								list2[0] = listsum(list1)-listsum(list2[1:])
								if listsum(list1)-listsum(list3[1:]) in available:
									list3[0] = listsum(list1)-listsum(list3[1:])
									a = printstring(list1, list2, list3)
									if a > maxstring:
										maxstring = a
'''

list1 = [10,0,0]

available = [1,2,3,4,5,6,7,8,9]

for i in itertools.permutations(available, 4):
	list2 = [i[0], 0, 0]
	list3 = [i[1], 0, 0]
	list4 = [i[2], 0, 0]
	list5 = [i[3], 0, 0]
	stillavailable = [1,2,3,4,5,6,7,8,9]
	stillavailable.remove(i[0])
	stillavailable.remove(i[1])
	stillavailable.remove(i[2])
	stillavailable.remove(i[3])
	for j in itertools.permutations(stillavailable, 5):
		if 10 + j[0] + j[1] == i[0] + j[1] + j[2] == i[1] + j[2] + j[3] == i[2] + j[3] + j[4] == i[3] + j[4] + j[0]:
			print [10,j[0],j[1]], [i[0], j[1], j[2]], [i[1], j[2], j[3]], [i[2], j[3], j[4]], [i[3], j[4], j[0]]
			
#print "Result: {}".format(maxstring)
print "Time: {}".format(time.clock()-start)