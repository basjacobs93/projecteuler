import time

start = time.clock()

triangles = [x*(x+1)/2 for x in range(20)]

f = open('/Users/Bas/Desktop/p042_words.txt', 'r')

number = 0

for word in f.read().split(","):
  som = 0
  for letter in word[1:-1]:
    som += ord(letter)-64
  if som in triangles:
    number += 1
    
print number

print time.clock() - start