import sys

# sys.setrecursionlimit(200500)
N = int(input())
sys.setrecursionlimit(N + 10)
g = [[] for i in range(N + 1)]
for i in range(N - 1):
    A, B = map(int, input().split())
    # 双方向リスト
    g[A].append(B)
    g[B].append(A)

visited = [False for i in range(N + 1)]
ans = []


def dfs(v):
    visited[v] = True

    ans.append(v)  # 初訪問

    for w in sorted(g[v]):  # 番号小さい順に訪問
        if not visited[w]:  # 未訪問なら行く
            dfs(w)
            # この戻ってくるのを加えるのが一番むずいかも
            ans.append(v)  # 戻ってきた


dfs(1)

print(*ans)
