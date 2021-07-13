A, B, X = map(int, input().split())

Max = -1
for l in range(1, 10):
    rest = X - 7 * l
    ans = rest // A
    if len(str(ans)) == l:
        Max = max(ans, Max)

print(Max)
