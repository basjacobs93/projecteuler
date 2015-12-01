sum = 0
f = 1
g = 1
h = 0
while h<4000000:
        h = f + g
        if h%2 == 0 and h<4000000:
                sum = sum + h
        f = g
        g = h
print (sum)
