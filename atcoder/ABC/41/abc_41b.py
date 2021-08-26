a,b,c = map(int,input().split())
mod = 10 ** 9 + 7
v1 = (a * b) % mod
v2 = (v1 * c) % mod
print(v2 % mod)