from collections import Counter

n, k = map(int, input().split())
c = list(map(int, input().split()))

counter = Counter(c[:k])
variety = len(counter)
ans = variety

for i in range(1, n-k+1):
    counter[c[i-1]] -= 1

    if counter[c[i-1]] == 0:
        variety -= 1

    if counter[c[i+k-1]] == 0:
        variety += 1

    counter[c[i+k-1]] += 1

    ans = max(ans, variety)
print(ans)