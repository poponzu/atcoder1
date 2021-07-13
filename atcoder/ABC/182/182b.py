N = int(input())
A = list(map(int, input().split()))
gcd = [0,0]

for k in range(2,1000):
    count =0
    for i in range(len(A)):
        if A[i]%k == 0:
            count += 1
    gcd.append(count)

print(gcd.index(max(gcd)))

