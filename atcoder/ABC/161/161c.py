n,k = map(int,input().split())

times = n//k + 1

ans = []

ans.append(abs(n - k * times))
ans.append(abs(n - k * (times - 1)))

print(min(ans))