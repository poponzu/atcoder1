# O(nloglogn)

N = int(input())

is_prime = [True] * (N + 1)
is_prime[0] = False
is_prime[1] = False
for i in range(2, N + 1):
    # is_primeがFalseならcontinue
    if not is_prime[i]:
        continue
    for j in range(2 * i, N + 1, i):
        is_prime[j] = False

ans = []
for i,x in enumerate(is_prime):
    if x:
        ans.append(i)

print(ans)