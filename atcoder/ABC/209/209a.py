a,b = map(int,input().split())

if a > b:
    print(0)
elif a == b:
    print(1)
else:
    print(b - a + 1)