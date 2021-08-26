a,b,c = map(int,input().split())
sum = a + b + c
M = max(a,b,c)

child = 3 * M - sum
# childの偶奇でchilｄのMを変えるところがすごい

if child % 2 == 0:
    print(child // 2)
else:
    child = (3 * (M+1)) - (sum)
    print(child // 2)