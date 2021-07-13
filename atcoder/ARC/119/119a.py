N=int(input())

a=0
B=0
c=0
ans = float("INf")

for b in range(60):
    B = 2**b
    a = N // B
    c = N - (a * B)
    ans = min(ans,a+b+c)

print(ans)
