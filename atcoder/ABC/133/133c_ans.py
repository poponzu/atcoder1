L,R = map(int,input().split())

mod = 2019
Min = float("INF")

for l in range(L, R):
    for r in range(l+1,R+1):
        ans = (l * r) % mod
        if ans == 0 :
            print(0)
            exit()
        Min = min(ans,Min)

print(Min)
