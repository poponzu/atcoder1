# 14:54 ~ 解けなかった
# 解説("https://blog.hamayanhamayan.com/entry/2018/02/18/224509")
# 解説の「0≦C[i][j]≦100なので、a1,a2,a3も[0,100]で探索すればいい。」が納得できひん。

# 入力
c = [list(map(int,input().split())) for _ in range(3)]

A = [0] * 3
B = [0] * 3

for a1 in range(0,101):
    for a2 in range(0,101):
        for a3 in range(0,101):
            b1 = c[0][0] - a1
            b2 = c[0][1] - a1
            b3 = c[0][2] - a1

            A[0] = a1
            A[1] = a2
            A[2] = a3
            B[0] = b1
            B[1] = b2
            B[2] = b3

            rule_ok = True
            for i in range(3):
                for j in range(3):
                    if A[i] + B[j] != c[i][j]:
                        rule_ok = False
            if rule_ok:
                print("Yes")
                exit()

print("No")