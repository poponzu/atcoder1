# おまじない
import sys
sys.setrecursionlimit(200500)

# 入力の読み込み
N, M = map(int, input().split())
G = [[] for i in range(N)]

for i in range(M):
    A, B = map(int, input().split())
    G[A-1].append(B-1)
    G[B-1].append(A-1)

def dfs(v):
    seen[v] = True
    for next_v in G[v]:
        if seen[next_v]:
            continue
        dfs(next_v)

cnt = 0 # 連結成分の個数
seen = [False] * N

for v in range(N):
    if seen[v]:
        continue
    dfs(v)
    # dfs(v) が呼ばれるときは、毎回「新たな連結成分内の頂点 v」が呼び出されていることになる。
    #  dfs(v) を呼び出すタイミングで counter をインクリメントすれば、counter の値が求める連結成分数となる
    cnt += 1

print(cnt - 1)