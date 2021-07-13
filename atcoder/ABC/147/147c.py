import itertools
from itertools import product

N = int(input())

person = list(product([True, False], repeat=N))

# print(len(person))
ans = -1
caution = [0] * 2**N

for i in range(N):
    A = int(input())
    # 競合が起きていたら警告数をみて答えを更新しない
    for _ in range(A):
        x, y = map(int, input().split())
        # その人が正直者なら忠実に実行
        # 競合が起きたらbitをすすめなあかん
        for bit in range(2 ** N):
            chara = [0] * N
            if person[bit][A - 1] == True:
                if y == 1:
                    # 競合が起きていたら警告＋１
                    if chara[x - 1] == False:
                        caution[bit] += 1
                    else:
                        chara[x - 1] = True
                else:
                    if chara[x - 1] == True:
                        caution[bit] += 1
                    else:
                        chara[x - 1] = False

for i in range(2 ** N):
    if caution[i] == 0:
        ans = max(ans, sum(person[i]))

print(ans)
