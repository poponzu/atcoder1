N, K = map(int, input().split())
# print(N,K)
p = list(map(int, input().split()))
# print(p)
print(p[:2])
print(p[:5])
# p[:K]はpというリストの前からK番目までを表してる
# pythonのスライスって検索すればでる
# 1 から P までの P 種類の目が等確率で出るサイコロの出目の期待値は (1 + P)/2 です。
# よくわからん　2/12理解した

ans = sum(p[:K])
cur = ans
for i in range(K,N):
    cur += p[i] - p[i-K]
    if cur > ans:
        ans = cur
print((ans + K)/2)