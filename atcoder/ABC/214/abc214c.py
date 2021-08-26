N = int(input())
S = list(map(int,input().split()))
T = list(map(int,input().split()))

S = S + S
T = T + T

# 最初の時間
# このstartの位置がだめ 最初が毎回[0]からスタートとは限らない

start = min(T)
start_index = T.index(start)
ans = [0] * 2 * N
ans[start_index] = start
# print(start)
# これは
for i in range(N-1):
    carry = start + S[i+start_index]
    small = min(carry, T[i+start_index+1])
    ans[i+start_index+1] = small
    # print(small)
    start = small

last = ans[N:N + start_index] + ans[start_index:N]

for l in last:
    print(l)

