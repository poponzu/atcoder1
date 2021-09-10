# 入力
S = list(input())
N = int(input())
L = []
R = []
for _ in range(N):
    l, r = map(int, input().split())
    L.append(l)
    R.append(r)

T = [0] * len(S)

for i in range(N):

    # lengthは何回書き込むかを表すtimesという名前でもよいかも？
    length = R[i] - L[i] + 1

    # S[l],S[l+1],・・・S[r]を１文字ずつT[r],T[r+1],・・・T[l]に書き込む
    for j in range(length):
        T[R[i]-1-j] = S[L[i]-1+j]

    # T[l],T[l+1],・・・T[r]を１文字ずつS[l],S[l+1],・・・S[r]に書き込む
    for k in range(L[i]-1,R[i]):
        S[k] = T[k]


print("".join(S))