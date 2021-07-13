n = int(input())

#約数列挙O(sqrt(N))リストで返す
def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]
list = make_divisors(n)
if len(list) % 2 == 0:
    x = list[len(list)//2 - 1]
    y = list[len(list)//2]
else:
    x = list[len(list)//2]
    y = x

ans = (x - 1) + (y - 1)

print(ans)
