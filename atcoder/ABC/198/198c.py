import math

R,X,Y = map(int, input().split())

#(X,Y)の原点からの距離をdとする
d = math.sqrt(X**2+Y**2)

if d%R ==0:
    ans= str(d//R)
    delete = ans.index(".")
    print(ans[:delete])
else:
    if R>d:
        print('2')
        exit()
    ans = str((d//R)+1)
    delete = ans.index(".")
    print(ans[:delete])