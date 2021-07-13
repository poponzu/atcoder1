n = int(input())

ans = float("INF")

for i in range(1,10**6 + 1):
    if n%i ==0:
        ans = min (ans,(i + n // i) - 2 )

print(ans)