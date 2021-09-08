import heapq

N, K = map(int, input().split())
A = list(map(int, input().split()))
# 最大値をとりだせるように
A = list(map(lambda x: x*(-1), A))
# a = list(map(lambda x: x*(-1), a))  # 各要素を-1倍
heapq.heapify(A)

tot = 0
for _ in range(K):
    # 最大値取り出す
    excite = heapq.heappop(A) * (-1)
    tot += excite
    heapq.heappush(A,(excite - 1) * (-1))

print(tot)
