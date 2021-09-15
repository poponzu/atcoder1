# 13:40~13:45

n = int(input())
a = list(map(int,input().split()))
sum = 0

for i in range(n-1):
    sum += a[i+1] - a[i]
    # print(a[i+1] - a[i])

# n-1に()をつけ忘れて結果がバグった
# print(sum)
ans = sum / (n-1)

print(ans)
