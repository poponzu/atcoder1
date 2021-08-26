import math

S = input()
K = int(input())

# K文字目までみる
# 1以外があればK文字目はS[i]確定
# 2 ** 5000兆 > 10 ** 18 (Kの最大値)だから
for i in range(K):
    if S[i] != "1":
        print(S[i])
        exit()

print(1)



