N = int(input())
S = list(map(int, input().split()))
T = list(map(int, input().split()))

for i in range(N):
    T[(i+1)%N] = min(T[(i+1)%N], T[i%N] + S[i%N])

for i in range(N):
    T[(i+1)] = min(T[(i+1)], T[i%N] + S[i%N])

for ans in T:
    print(ans)
