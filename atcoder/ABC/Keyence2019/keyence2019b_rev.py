S = input()
T = "keyence"
j = 0

for i in range(len(S)):
    if j <= 6:
        if S[i] == T[j]:
            j += 1

if j >= 7:
    print("YES")
else:
    print("NO")