X, Y = map(int, input().split(sep="."))
# print(X, Y)
if 0 <= Y <= 2:
    print(str(X) + "-")
elif 3 <= Y <= 6:
    print(str(X))
else:
    print(str(X) + "+")
