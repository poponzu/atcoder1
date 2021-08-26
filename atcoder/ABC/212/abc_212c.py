import bisect

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# sort_B = sorted(B)
B.sort()
Min = B[0]
Max = B[-1]

# 取り得る最大値が10**9 - 1 だから最小値の初期値はあってるはず
ans = 10 ** 18

# aを全探索
for a in A:
    # if M == 1:
    #     ans = min(ans, abs(a - B[0]))
    if a < Min:
        ans = min(ans, abs(a - Min))
    elif a > Max:
        ans = min(ans, abs(a - Max))
    else:
        place = bisect.bisect_left(B, a)
        # ここの探索対象の配列の変数を間違っていた
        # 今まで破壊的なソートを使っていなかったけど、ソートしたものをつかうことが多いから破壊的処理の方も使っていこう
        ans = min(ans, abs(a - B[place]))
        ans = min(ans, abs(a - B[place - 1]))

print(ans)
