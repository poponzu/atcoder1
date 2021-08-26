S = input()
L = len(S)
ans = 1
# 末尾の偶数文字ずつ消去 -> O(N)
for i in range(L - 2, 0, -2):
    pattern = S[:i]
    pl = len(pattern)
    # 偶文字列判定 -> O(N)
    if pattern[:pl // 2] == pattern[pl // 2:]:
        ans = max(ans, i)

# aaとか来たときans = 0のままではだめだからans修正
# ansの初期化を1にすることで不必要になった
# if ans == 0:
#     ans = 1

print(ans)
