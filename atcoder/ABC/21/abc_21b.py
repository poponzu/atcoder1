# 6分AC

N = int(input())
a, b = map(int, input().split())
K = int(input())
P = list(map(int, input().split()))

P.append(a)
P.append(b)
l = len(P)
P = set(P)
P = list(P)

if len(P) == l:
    print("YES")
else:
    print("NO")
