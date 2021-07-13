N= int(input())
import math

#素数判定 O(sqrt(N))
def bool_is_prime(x):
    if x<=1:
        return False
    for i in range(2,math.floor(math.sqrt(x))+1):
        if x%i == 0:
            return False
    return True

p = N
while bool_is_prime(p)==False:
    p += 1

print(p)