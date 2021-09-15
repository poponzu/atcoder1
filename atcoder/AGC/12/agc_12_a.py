# input

# 「2, 4, 6, . . . , 2N 番目に強い参加者の強さの和

N = int(input())
a = list(map(int,input().split()))

a.sort(reverse=True)
# print(a)

sum = 0

for i in range(1,2*N,2):
    sum += a[i]

print(sum)