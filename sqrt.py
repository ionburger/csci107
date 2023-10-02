def mySqrt(n):
    oldguess = n/2
    for i in range(100):
        newguess = (1/2) * (oldguess+(n/oldguess))
        oldguess = newguess
    return newguess
print(mySqrt(int(input(""))))