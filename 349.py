#!/usr/bin/python
import time
width = 10000
height = 7000
steps = 12000

matrix = [["."] * width for _ in xrange(height)]
# 0 = white
# 1 = black

ant = [width/2, height/3]
dirs = [(-1,0),(0,1),(1,0),(0,-1)]
direction = 0

counter = 0
counterlist = [0]*105
i = 0
j = 0
while j<steps and 0<=ant[0]<height and 0<=ant[1]<width:
	if matrix[ant[0]][ant[1]] == ".":
		matrix[ant[0]][ant[1]] = "x"
		direction = (direction+1)%4
		ant[0] += dirs[direction][0]
		ant[1] += dirs[direction][1]
		counter += 1
	else:
		matrix[ant[0]][ant[1]] = "."
		direction = (direction-1)%4
		ant[0] += dirs[direction][0]
		ant[1] += dirs[direction][1]
		counter -= 1
	counterlist[i] = counter
	j += 1
	if j==10440:
		print counter
		break
	#print counterlist[i], counterlist[i]- counterlist[(i-104)%105]
	i = (i+1)%105
	
# we see that eventually it has period 104, increasing 12
# 10**18 % 104 = 40
# 40+104*100 = 10440
# hence the number of black tiles at time 10**18 is equal to the amount at time 10440
# but we have to add 12*(10^18-10440)/104 = 115384615384614180
# the amount at time 1080 is 772, so we get 115384615384614180+772=115384615384614952