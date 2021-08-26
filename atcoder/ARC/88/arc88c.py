x, y = map(int, input().split())
ans = 1
# 対数計算ミスってた
# 検算にpythonで書いてcheckしようこれから
# 発想は間違っていなかった。

for i in range(60):
    result = x * (2 ** i)
    if result <= y:
        ans = max(ans, i + 1)

print(ans)
