#解説https://blacktanktop.hatenablog.com/entry/2020/07/06/202932
import copy
import itertools
from itertools import product

# itertoolsを使ってパターンを列挙して考える方法
H, W, K = map(int, input().split())
# あとで足し算で計算するので#は1にそれ以外は0へ
C = [[1 if v == '#' else 0 for v in input()] for _ in range(H)]
ans = 0
# 塗り直すか塗り直さないかの01のパターンを出す
HC = list(product([0, 1], repeat=H))
WC = list(product([0, 1], repeat=W))
# 選んだところは0に塗り直す
c = copy.deepcopy(C)
# hcは塗る行タプル（indexが行目、1だと塗る）
for hc in HC:
    # wcは塗る列タプル（indexが列目、1だと塗る）
    for wc in WC:
        count = 0
        # hiが行目
        for hi, h in enumerate(hc):
            if h == 1:
                for w in range(W):
                    c[hi][w] = 0
        # wiが列目
        for wi, w in enumerate(wc):
            if w == 1:
                for h in range(H):
                    c[h][wi] = 0
        # flatten
        count = sum(list(itertools.chain.from_iterable(c)))
        if count == K:
            ans += 1
        # 次のループのために初期化
        c = copy.deepcopy(C)
print(ans)
