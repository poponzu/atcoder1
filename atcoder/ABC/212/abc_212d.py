import heapq  # heapqライブラリのimport

a = []
heapq.heapify(a)

Q = int(input())
L = [list(map(int, input().split())) for _ in range(Q)]
add = 0

for i in range(Q):
    if L[i][0] == 1:
        heapq.heappush(a, L[i][1] - add)  # 要素の挿入

    elif L[i][0] == 2:  # 出力するときの今まで何回操作2があり数字を加えなければいけないか
        # このままだと自分が袋にいなかったときの操作2の加算が入ってしまう
        add += L[i][1]
    else:
        print(heapq.heappop(a) + add)

# heapq.heapify(a)  # リストを優先度付きキューへ
