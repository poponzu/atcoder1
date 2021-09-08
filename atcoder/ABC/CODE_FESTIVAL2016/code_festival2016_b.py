# 10分AC

N = int(input())
a = list(map(int, input().split()))

seen = [False] * N

cnt = 0
# a_ai = i を満たすiを数える
# 1ペアにつき二回数えてしまうから最後に２で割る
for i in range(N):
    if a[a[i] - 1] == i+1:
        cnt += 1

print(cnt//2)
