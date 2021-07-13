import sys
sys.setrecursionlimit(10000)

# 入力の読み込み
N, M = map(int, input().split())
G = [[] for i in range(N)]

for i in range(M):
    A, B ,C= map(int, input().split())
    G[A-1][B-1] = C

def f(s,t,k):
    goal = t
    dfs()