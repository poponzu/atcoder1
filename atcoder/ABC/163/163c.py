N=int(input())
A=list(map(int,input().split()))

ans =[0] * N
#なんこ１〜Nが配列中にあるか数えるだけ

for i in range(N-1):
    ans[A[i]-1] += 1

for i in ans:
    print(i)