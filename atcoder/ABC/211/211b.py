s1 = input()
s2 = input()
s3 = input()
s4 = input()

cnt1 = 0
cnt2 = 0
cnt3 = 0
cnt4 = 0

S = []

S.append(s1)
S.append(s2)
S.append(s3)
S.append(s4)

ans = set(S)
ans = list(ans)

if len(ans) == 4:
    print("Yes")
else:
    print("No")
