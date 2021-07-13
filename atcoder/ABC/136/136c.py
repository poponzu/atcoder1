#12分くらいAC
N = int(input())

H = list(map(int,input().split()))

Max = 0
for i in range(N):
    Max = max(H[i], Max)
    if H[i] < Max - 1:
        print("No")
        exit()

print("Yes")