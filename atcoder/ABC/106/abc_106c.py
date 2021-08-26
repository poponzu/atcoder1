# 9分AC
# コードミスってるまぐれAC

S = input()
K = int(input())

count = 0
for s in S:
    s = int(s)
    # ここがオーバーフローするか不安やった
    count += s ** 5000
    if count >= K:
        print(s)
        exit()
