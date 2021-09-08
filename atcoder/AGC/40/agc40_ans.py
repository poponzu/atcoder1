S = input()
n = len(S) + 1
a = [0] * (n)
for i in range(n-1):
    if S[i] == "<":
        a[i+1] = max(a[i] + 1, a[i + 1])
# print(a)

# print(sum(a))
for i in range(n-2,-1,-1):
    if S[i] == ">":
        a[i] = max(a[i+1]+1, a[i])

# print(a)
print(sum(a))
