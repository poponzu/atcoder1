N = input()

K = len(N)
C = N[0]

check = N[1:]

# cとCの変数が同じ名前になって答えが合わなくなってた
# 変数は同じもの使わないようにする
# ノートに書こう
all9 = True
for c in check:
    if c != "9":
        all9 = False
# all9 = Trueならnの形はc9999..99という形

if all9:
    ans = int(C) + 9 * (K - 1)
else:
    ans = int(C) + 9 * (K - 1) - 1

print(ans)

#
# S = "19"
# print(S[0])