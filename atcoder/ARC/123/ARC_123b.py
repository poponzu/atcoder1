import heapq

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

A.sort()
B.sort()
C.sort()

heapq.heapify(A)
heapq.heapify(B)
heapq.heapify(C)

ans = 0

# なぜ計算量がO(nlogn)なのかきっちり考える
while len(A) != 0:
    a = A[0]
    heapq.heappop(A)

    while len(B) != 0 and B[0] <= a:
        heapq.heappop(B)
    if len(B) == 0:
        break
    b = B[0]
    heapq.heappop(B)

    while len(C) != 0 and C[0] <= b:
        heapq.heappop(C)
    if len(C) == 0:
        break
    c = C[0]
    heapq.heappop(C)

    ans += 1

print(ans)
