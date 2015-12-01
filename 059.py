import math, time

start = time.clock()

def decypher(text, key):
  ln = ""
  for a in range(len(text)):
    ln += chr(int(text[a])^key[a%3])
  if " and " in ln:
    sm = 0
    for i in range(len(ln)):
      sm += ord(ln[i])
    return sm
  return 0
  
f = open("/Users/Bas/Desktop/p059_cipher.txt", "r")
spltf = f.read().split(',')

for a in range(97,123):
  for b in range(97,123):
    for c in range(97,123):
      ans = decypher(spltf, [a, b, c])
      if ans > 0:
        print ans, chr(a), chr(b), chr(c)
        print time.clock()-start
        quit()