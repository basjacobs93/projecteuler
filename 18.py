import math, itertools

triangle = [[75], [95, 64], [17, 47, 82], [18, 35, 87, 10], [20, 04, 82, 47, 65], [19, 1, 23, 75, 3, 34], [88, 2, 77, 73, 7, 63, 67], [99, 65, 4, 28, 6, 16, 70, 92], [41, 41, 26, 56, 83, 40, 80, 70, 33], [41, 48, 72, 33, 47, 32, 37, 16, 94, 29], [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14], [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57], [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48], [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31], [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]]

def tryroute(route, triangle):
  j = 0
  sum = triangle[0][0]
  numbers = [triangle[0][0]]
  for i in range(1, len(triangle)):
    j = route[i-1]+j
    numbers += [triangle[i][j]]
    sum += triangle[i][j]
  return sum, numbers

max = 0
routes = itertools.product([0,1], repeat=len(triangle)-1)
for route in routes:
  new = tryroute(route, triangle)
  if new[0] > max:
    max = new[0]
    numbers = new[1]

print max, numbers