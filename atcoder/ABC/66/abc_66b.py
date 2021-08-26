S = input()
L = len(S)
# 末尾のi文字消去(i >= 1) -> O(N)
for i in range(L - 1, 0, -1):
    pattern = S[:i]
    pl = len(pattern)
    if pl != 1 and pl % 2 == 1:
        continue
    elif pl % 2 == 0:
        # 偶文字列判定 -> O(N**2)?
        if pattern[:pl // 2] == pattern[pl // 2:]:
            print(pl)
            exit()
    else:
        print(pl)
        exit()
