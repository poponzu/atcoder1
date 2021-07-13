N = int(input())
DP =[0] * N
A=[]
for _ in range(N):
    a = list(map(int,input().split()))
    A.append(a)

DP[0] = max(A[0])
action = A[0].index(max(A[0]))
#action = 0,1,2

#actionの保存方法にバグがありそう

for i in range(1,N):
    if action == 0:
        A[i]=A[1:3]
        DP[i] = DP[i-1] + max(A[i])
        action = A[i].index(DP[i]-DP[i-1])
    elif action == 1:
        DP[i] = DP[i-1] +max(A[i][0],A[i][2])
        #actionの値が更新されていない
        action = A[i].index(DP[i]-DP[i-1])
    else:
        DP[i] = DP[i - 1] + max(A[i][0], A[i][1])
        action = A[i].index(DP[i]-DP[i-1])

print(DP[-1])