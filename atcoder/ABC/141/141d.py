import heapq

n, m = map(int, input().split())
a = list(map(int, input().split()))

# リストを最大値を取得できる優先度付きキューに
a = list(map(lambda x: x * (-1), a))  # 各要素を-1倍
heapq.heapify(a)

# 最大値の取り出し
for _ in range(m):
    heapq.heappush(a, (heapq.heappop(a) * (-1) // 2) * -1)

# 最後キューの中身全部足す
# a = list(map(lambda x: x * (-1), a))
# print(sum(a))

a = list(a)
print(-sum(a))