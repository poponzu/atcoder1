# from math import factorial
#
# N =int(input())
# result = 0
#
# if N==1:
#     print(0)
#     exit()
#
# result = ((factorial(N) // factorial(2) // factorial(N - 2))* 2 * (10**(N-2)))%(10**9+7)
#
# print(result)

m = 1000000007

N = int(input())

print((pow(10, N, m) - pow(9, N, m) * 2 + pow(8, N, m)) % m)




