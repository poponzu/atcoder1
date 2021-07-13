N,M = map(int,input().split())
H = list(map(int,input().split()))

#隣接する展望台のもっとも高い値が入っているリスト
T = [0] * N

for _ in range(M):
    A,B = map(int,input().split())
    T[A-1] = max(T[A-1],H[B-1])
    T[B-1] = max(T[B-1],H[A-1])

count = 0
for i in range(N):
    if H[i] > T[i]:
        count += 1

print(count)