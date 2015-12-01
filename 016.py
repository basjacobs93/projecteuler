number = 2**1000
length = len(str(number))

digitsum = 0
for i in range(length):
    digitsum += int(str(number)[i])
print(digitsum)
