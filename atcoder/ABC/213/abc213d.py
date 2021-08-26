# おまじない
import sys
sys.setrecursionlimit(300000)

N=int(input())
G=[[] for i in range(N+1)]
for i in range(N-1):
    a,b=map(int,input().split())
    G[a].append(b)
    G[b].append(a)

# そのような都市のうち番号が最も小さい都市へ移動するを満たすためである。
for i in range(N+1):
    G[i].sort()

ans=[]
# crr preってなにを表す？
def dfs(crr,pre):
    ans.append(crr)
    for nxt in G[crr]:
        if nxt!=pre:
            dfs(nxt,crr)
            ans.append(crr)

dfs(1,-1)
print(*ans)