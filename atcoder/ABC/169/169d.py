# import sympy

N = int(input())



def divisor(n):
    i = 1
    table = []
    while i * i <= n:
        if n % i == 0:
            table.append(i)
            table.append(n // i)
        i += 1
    table = list(set(table))
    return table

# a = sympy.divisors(N)

print(sorted(divisor(N)))


