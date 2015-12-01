def factorial(n):
    if n==1:
        return 1
    else:
        return n*factorial(n-1)

number = factorial(100)
length = len(str(number))

digitsum = 0
for i in range(length):
    digitsum += int(str(number)[i])
print(digitsum)
