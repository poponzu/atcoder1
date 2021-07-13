n, k = map(int, input().split())
a = list(map(int, input().split()))

# 0 から (2^n)-1 までループ
for bit in range(2**n):
    sum = 0
    for i in range(n):# このループが一番のポイント
        if (bit >>i) & 1 : # 順に右にシフトさせ最下位bitのチェックを行う
            # フラグが立っているならば sum に加算する
            sum += a[i]

    if sum == k:
        print("Yes")
        exit()

print("No")