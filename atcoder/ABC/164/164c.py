N = int(input())
S=[]
for _ in range(N):
    s = input()
    S.append(s)

ans = set(S)

print(len(ans))