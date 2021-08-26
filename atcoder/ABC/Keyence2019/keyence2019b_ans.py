S = input()
L = len(S)

flag = False

# 全探索の部分納得できひん
# i文字目からj文字目まで削除する場合を全て考える
for i in range(L):
    for j in range(i, L):
        made = S[:i] + S[j:]
        if made == "keyence":
            flag = True

if flag:
    print("YES")
else:
    print("NO")
