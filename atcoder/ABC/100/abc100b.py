# 19分AC
# d =0,1,2における n == 100のときの場合を考えるのに苦労

d,n = map(int,input().split())

if d == 0:
    if n == 100:
        print(101)
        exit()
    else:
        print(100 ** d * n)
elif d == 1:
    if n == 100:
        print(10100)
    else:
        print(100 ** d * n)
else:
    if n == 100:
        print(1010000)
    else:
        print(100 ** d * n)