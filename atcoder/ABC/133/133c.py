L,R = map(int,input().split())

ans = 0
mod = 2019

Min = float("INF")

if R - L >= 2019:
    Min = 0
else:
    for l in range(L,R):
        for r in range(l+1,R+1):
            ans = (l * r) % mod
            Min = min(ans ,Min)


print(Min)





