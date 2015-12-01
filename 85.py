#!/usr/bin/python
'''
1x1	1
2x1	3
3x1	6
4x1	10
5x1	15

1x2	3		3* (1x1)
2x2	9		3* (2x1)
3x2	18
4x2	30

1x3	6		6* (1x1)
2x3	18		6* (2x1)
3x3	36

1x4	10		10* (1x1)
2x4	30		

m x n:	(n*(n+1)/2)*(m*(m+1)/2)
'''
def counter(n,m):
	return (n*(n+1)/2)*(m*(m+1)/2)
	
closest = 2000000
closest_i = 0
closest_j = 0
for i in range(2000):
	for j in range(i):
		if abs(2000000-counter(i,j))<closest:
			closest = abs(2000000-counter(i,j))
			closest_i = i
			closest_j = j

print closest_i, closest_j, closest_i*closest_j, counter(closest_i,closest_j)