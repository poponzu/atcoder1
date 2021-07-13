a, b = map(int, input().split())

d = a//b
r = a%b
f = a/b

#print("{0} {1} {2:.9f}".format(d, r, f))
print(f"{d} {r} {f:.9f}")