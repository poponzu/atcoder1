# キューを使った方法
import collections

N, K =map(int,input().split())
A = list(map(int,input().split()))

d = collections.deque()

# 初期のキュー
for i in range(K):
    d.appendleft(A[i])

ans =  sum(d)
sum_ = sum(d)

for j in range(N - K):
    out = d.pop()
    sum_ -= out
    in_ = A[j + K]
    sum_ += in_
    d.appendleft(in_)
    ans += sum_

print(ans)