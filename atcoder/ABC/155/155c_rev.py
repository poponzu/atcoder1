from collections import Counter

N = int(input())
S = []
for _ in range(N):
    S.append(input())

S = Counter(S)

max = max(S.values())

ans =[]
for k,v in S.items():
    if v == max:
       ans.append(k)

ans = sorted(ans)
for i in ans:
    print(i)