N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

only=[]

for a in A:
    if a not in B:
        only.append(a)

for b in B:
    if b not in A:
        only.append(b)

new_only = sorted(only)

print(*new_only)