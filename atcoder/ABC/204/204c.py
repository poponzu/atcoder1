# おまじない
import sys
sys.setrecursionlimit(10000)

# 入力の読み込み
N, M = map(int, input().split())
G = [[] for i in range(N)]
# G[i] は都市iから道路で直接繋がっている都市のリスト
for i in range(M):
    A, B = map(int, input().split())
    G[A - 1].append(B - 1)


# dfs
def dfs(v):
    seen[v] = True
    # vから行ける各頂点next_vについて
    for next_v in G[v]:
        if seen[next_v]:
            continue
        dfs(next_v)


ans = 0

# 都市iからスタートする場合
for i in range(N):
    seen = [False] * N
    # temp[j] は都市jに到達可能かどうかを表す
    dfs(i)
    ans += sum(seen)

print(ans)
