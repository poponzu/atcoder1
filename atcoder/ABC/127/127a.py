A, B = map(int,input().split())

if A >= 13:
    print(B)
    exit()
elif 6 <= A <= 12:
    print(B//2)
else:
    print(0)