
#解説("https://nekotheshadow.hatenablog.com/entry/2020/06/16/001107")
x, n = map(int, input().split())
p = set(map(int, input().split()))
#print(p)
d = 0
while True:
    if not x - d in p:
        print(x - d)
        break

    if not x + d in p:
        print(x + d)
        break

    d += 1
