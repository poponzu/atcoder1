import math
N=int(input())
s=set()

for a in range(2,int(math.sqrt(N))+1):
    for b in range(2,N+1):
        t=a**b
        if t>N:
            break
        s.add(t)

print(N-len(s))




