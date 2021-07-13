#17分AC
#解説の考え方2がようわからん
N, M = map(int,input().split())

ansL = -1
ansR = 10**6

for _ in range(M):
    L, R = map(int,input().split())
    ansL = max(L, ansL)
    ansR = min(R, ansR)
    #ここのケースを見つけるのに10分くらいかかってしまった
    if ansL > ansR:
        print(0)
        exit()

print(ansR - ansL + 1)