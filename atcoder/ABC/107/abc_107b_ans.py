# 自分の解法と比べてスマートすぎる

h, w = map(int, input().split())
a = [''] * h
for i in range(h):
    a[i] = input()

# 各行、各列に対して黒点が一つでもあるかどうか調べる
row = [False] * h
col = [False] * w
for i in range(h):
    for j in range(w):
        if a[i][j] == "#":
            row[i] = True
            col[j] = True

# 感覚的にはわかるけど、しっくり来てない
for i in range(h):
    if row[i]:
        for j in range(w):
            if col[j]:
                print(a[i][j], end ="")
        print()