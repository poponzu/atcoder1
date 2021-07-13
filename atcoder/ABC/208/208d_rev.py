# ABC035 D トレジャーハント

import heapq

def dijkstra(s, n, c_list):
    _list = [float("Inf")]*n
    _list[s] = 0
    hq = [[0,s]]
    heapq.heapify(hq)
    while len(hq) > 0:
        _ci, _i = heapq.heappop(hq)
        if _list[_i] < _ci:
            continue
        for _cj,_j in c_list[_i]:
            if _list[_j] > (_list[_i] + _cj):
                _list[_j] = _list[_i] + _cj
                heapq.heappush(hq, [_list[_j],_j])
    return _list

n, m = map(int, input().split())
a_list = [int(x) for x in input().split()]
g_list = [[] for i in range(n)]
b_list = [[] for i in range(n)]

for i in range(m):
    _a, _b, _c = map(int, input().split())
    g_list[_a-1].append([_c,_b-1])
    b_list[_b-1].append([_c,_a-1])

go = dijkstra(0, n, g_list)
back = dijkstra(0, n, b_list)
ans = 0

for i in range(n):
    _tmp = t - (go[i] + back[i])
    if a_list[i]*_tmp > ans:
        ans = a_list[i]*_tmp

print(ans)