import math
while True:
    n = int(input())
    if n==0:
        break

    s = list(map(float, input().split()))
    average = sum(s)/len(s)
    numerator = 0
    for i in range(n):
        numerator +=(s[i]-average)**2
    print(math.sqrt(numerator/n))
