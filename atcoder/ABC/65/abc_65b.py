N = int(input())
A  = []
for _ in range(N):
    a = int(input())
    A.append(a)

light2 = False
cnt = 1

i = 0
# まずのボタン1押す
# A[0]が光る
while A[i] != 2:
    i = A[i] - 1
    # ボタンA[i]を押す
    cnt += 1
    # このループ抜ける条件これでいいの？
    if cnt >= 10**5:
        break
else:
    light2 = True

if light2:
    print(cnt)
else:
    print(-1)