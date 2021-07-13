A,B, C,K = map(int, input().split())
count = 0
sum = 0
for a in range(A):
    sum = sum + 1
    count = count + 1
    if count >= K:
        break



for b in range(B):
    if count >= K:
        break
    sum = sum + 0
    count = count + 1




for c in range(C):
    if count >= K:
        break
    sum = sum - 1
    count = count + 1


print(sum)