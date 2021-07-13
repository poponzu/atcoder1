rows = int(input())
S = set([input() for i in range(rows)])

for s in S:
    if "!"+s in S:
        print(s)
        exit()
print("satisfiable")
