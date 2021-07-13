N = int(input())

count =0

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

for C in range(1,N):
    N_prime = N-C
    count += len(make_divisors(N_prime))

print(count)

