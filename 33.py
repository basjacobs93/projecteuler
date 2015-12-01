def cancelterms(num1, num2, term):
  if term not in num1 or term not in num2:
    return -1
  try:
    num1 = num1.replace(term, "", 1)
    num2 = num2.replace(term, "", 1)
    return float(num1) / float(num2)
  except:
    return -1

solution = 1

for den in range(10, 100):
  for num in range(10, den):
    for j in range(1, 10):
      if cancelterms(str(num), str(den), str(j)) == float(num)/float(den):
        solution *= float(num)/float(den)
        print num, den
        
print solution