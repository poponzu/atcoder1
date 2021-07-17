N = int(input())
A = []
for _ in range(N):
    a = int(input())
    A.append(a)

set_A = set(A)
list_A = list(set_A)
sort_A = sorted(list_A,reverse=True)

print(sort_A[1])


