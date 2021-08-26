# 9分AC
import itertools

S = input()
# 小文字に統一
S = S.lower()
l = len(S)

comb = list(itertools.combinations(range(l),3))

for c in comb:
    make = S[c[0]] + S[c[1]] + S[c[2]]
    if make =="ict":
        print("YES")
        exit()

print("NO")