import sys
input =sys.stdin.readline

N=int(input())
S=list(input())
S.pop()
Q=int(input())

Query= [list(map(int, input().split())) for i in range(Q)]
for qnumber in range(Q):
    #文字入れ替え
    if Query[qnumber][0]==1:
        S[(Query[qnumber][1]-1)],S[(Query[qnumber][2]-1)] = S[(Query[qnumber][2]-1)],S[(Query[qnumber][1]-1)]
    # 文字前後入れ替え
    #高速にできないか？
    elif Query[qnumber][0]==2:
        S= S[N:]+S[:N]

print("".join(S))




