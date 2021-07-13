N, M = map(int, input().split())

ks = []
for _ in range(M):
    column = list(map(int, input().split()))
    ks.append(column)

p = list(map(int, input().split()))
ans = 0

for i in range(2 ** N):
    switch = [False] * N
    light = 0

    for j in range(N):
        # フラグが立ってたらスイッチon
        if (i >> j) & 1:
            switch[j] = True

    # スイッチの状態決定
    for k in range(M):
        # 最初countの初期化をもう1行上でやってたせいでWA
        count = 0
        for l in range(1, ks[k][0] + 1):
            if switch[ks[k][l] - 1]:
                # 各電球について、 on になっているスイッチの個数を数える
                count += 1
        # onになってるスイッチの数を2で割った余りが p[k]の値と等しいと点灯
        if count % 2 == p[k]:
            light += 1

    # 全ての電球が点灯するなら ans + 1
    if light == M:
        ans += 1

print(ans)
