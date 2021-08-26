# WAになる例がわからん
# 削除区間が二つのときのNOでもYESと出力しちゃう
# 例 zkzeyence 正しくはNOなのにこのコードだとYESとでてしまう


from collections import deque

S = input()
T = "keyence"
T = deque(T)

for i in range(len(S)):
    #
    if S[i] == T[0]:
        T.popleft()
    if len(T) == 0:
        print("YES")
        exit()

print("NO")