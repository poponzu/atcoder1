# 時間計算量0(M)

N = int(input())
A = list(map(int, input().split()))

M = max(A) + 1

# 作業用の配列Cを用意
# カウンタをクリアする
C = [0] * M

# キーの個数を数える
for a in A:
    C[a] += 1


i = 0

# 計算量O(n)
for a in range(M):
    # aが何回出現しているかをCをみて繰り返す
    for _ in range(C[a]):
        A[i] = a
        i += 1

print(A)
