N,M = map(int,input().split())
S = list(map(int,input().split()))
T = list(map(int,input().split()))

distance = [-1] * N
start = 0
# 左から順に
for i in range(N-1):
    if S[i] != S[i+1]:
        # startからi+1まで全部S[i+1]に置き換えたい
        for j in range(start,i+1): # for文使うんやったらTLE？
            distance[j] = S[i+1]
        start = i+1
    else:
        start += 1

start = N
for i in range(N-1,1,-1):
    if S[i] != S[i-1]:
        # startからi+1まで全部S[i+1]に置き換えたい
        for j in range(start,i-1,-1): # for文使うんやったらTLE？
            distance[j] = S[j-1]
        start = i-1
print(distance)
