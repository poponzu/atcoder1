n = input()
op_cnt = len(n) - 1

for i in range(2 ** op_cnt):
    op = ["-"] * op_cnt
    for j in range(len(n) - 1):
        if ((i >> j) & 1):
            op[op_cnt - 1 - j] = "+"
    # スクリプトで送る
    ans = ""
    # [""]はリストにくっつける
    for x, y in zip(n, op + [""]):
        ans += (x + y)
    if eval(ans) == 7:
        print(ans + "=7")
        exit()
