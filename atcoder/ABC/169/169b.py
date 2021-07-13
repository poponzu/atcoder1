

n = int(input())
a = list(map(int, input().split()))
a.sort()
result = 1

for i in a:
    result = result * i

    # result = np.prod(a)

    if (result > pow(10, 18)):
        result = -1
        break

print(result)

# N=int(input())
# A=list(map(int,input().split()))
# A.sort()
# B=1
# for i in A:
#   B*=i
#   if(B>10**18):
#     B=-1
#     break
# print(B)
