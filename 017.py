def letterCount(n):
    sum = 0
    if n == 1000:
        sum = 11
    elif n<=15:
        if n==0:
            sum = 0
        elif n==1 or n==2 or n==6 or n==10:
            sum = 3
        elif n==4 or n==5 or n==9:
            sum = 4
        elif n==3 or n==7 or n==8:
            sum = 5
        elif n==11 or n==12:
            sum = 6
        elif n==15:
            sum = 7
        elif n==13 or n==14:
            sum = 8
    elif n<20:
        if n==18:
            sum = letterCount(n%10) + 3 #eighteen
        else:
            sum = letterCount(n%10) + 4 #seven + teen
    elif n<40:
        sum = 6 + letterCount(n%10)
    elif n<70:
        sum = 5 + letterCount(n%10)
    elif n<80:
        sum = 7 + letterCount(n%10)
    elif n<90:
        sum = 6 + letterCount(n%10)
    elif n<100:
        sum = 6 + letterCount(n%10)
    elif n>=100:
        sum += letterCount(n//100) #three
        sum += 7 #hundred
        if n%100 != 0:
            sum += 3 #and
            sum += letterCount(n%100) #fortytwo
    return sum

tot = 0
for n in range(1,1001):
    tot += letterCount(n)
print(str(tot))
