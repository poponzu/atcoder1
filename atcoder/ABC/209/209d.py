import queue

N, Q = map(int, input().split())
G = [[] for i in range(N)]
for i in range(N - 1):
    a, b = map(int, input().split())
    G[a - 1].append(b - 1)
    G[b - 1].append(a - 1)

que = queue.Queue()
color = [-1] * N
color[0] = 0
que.put(0)
while not que.empty():
    t = que.get()
    for i in G[t]:
        # 色分けは0と1の二種類で行う
        # color[i] = -1なら初訪問
        if color[i] == -1:
            # color[i] = 1 - color[t]は賢すぎる
            if color[t] == 0:
                color[i] = 1
            else:
                color[i] = 0
            que.put(i)

for i in range(Q):
    a, b = map(int, input().split())
    if color[a - 1] == color[b - 1]:
        print("Town")
    else:
        print("Road")
