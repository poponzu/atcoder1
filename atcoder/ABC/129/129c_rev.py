#貰うDPの方
#初期値と配列外参照には気をつけよう！
N, M = map(int,input().split())
A = []
for _ in range(M):
    a = int(input())
    A.append(a)

#DP[i]はi段目にたどり着く移動方法の数
DP =[1] * (N+1)
DP[0] = 1
mod = 10**9 + 7

#壊れている階段はには０を代入
for a in A:
    DP[a] = 0

#最初が壊れているかどうかでDP[1]の初期値が変化する
if M > 0:
    if A[0] != 1:
        DP[1] = 1
    else:
        DP[1] = 0

for i in range(2, N+1):
    if DP[i] == 0:
        continue
    else:
        j = i - 2
        k = i - 1
        if j >= 0 and k >= 0:
            DP[i] = (DP[j] + DP[k]) % mod

print(DP[-1])