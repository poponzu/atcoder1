N = int(input())
S = []
T = []
for _ in range(N):
    s,t = map(str,input().split())
    S.append(s)
    T.append(t)


duplicate = False

for i in range(N - 1):
    for j in range(i+1, N):
        if S[i] == S[j] and T[i] == T[j]:
            duplicate = True

if duplicate:
    print("Yes")
else:
    print("No")
