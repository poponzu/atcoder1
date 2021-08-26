from collections import deque

N, K = map(int, input().split())
d = deque()
A = list(map(int, input().split()))

ans = 0
# 初期状態
for i in range(K):
    d.append(A[i])

set_d = set(d)
ans = len(set_d)

length = ans

for i in range(K, N):
    out = d.popleft()
    set_d = set(d)
    # でていくやつがまだある
    if out in set_d:
        if A[i] in set_d:
            length += 0
        else:
            length += 1
    # でていくやつが最後の一つ
    else:
        if A[i] in set_d:
            length += -1
        else:
            length += 0

    ans = max(length, ans)
    d.append(A[i])

print(ans)
