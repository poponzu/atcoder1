import itertools
import math

N = int(input())
X = []
Y = []

for _ in range(N):
    x,y = map(int,input().split())
    X.append(x)
    Y.append(y)

city =[]
for i in range(N):
    city.append(i)

P = itertools.permutations(city, N)

sum = 0
for p in P:
    for i in range(N-1):
       sum +=  math.sqrt(((X[p[i]] - X[p[i+1]]) ** 2 ) + ((Y[p[i]] - Y[p[i+1]]) ** 2))

print(sum/math.factorial(N))






