# import math
# print(math.log(10**18,2))
N = int(input())
ans = []
while N > 0:
    if N % 2 == 1:
        N -= 1
        ans.append("A")
    else:
        N //= 2
        ans.append("B")

# print(ans)
ans.reverse()
print("".join(ans))
