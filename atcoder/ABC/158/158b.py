# N,A,B=map(int,input().split())
# # print(N)
# List = []
# n = 0
# while n < N:
#     for a in range(A):
#         List.append('b')
#         n = n + 1
#         if n >= N:
#             break
#     for b in range(B):
#         if n >= N:
#             break
#         List.append('r')
#         n = n + 1
#         if n >= N:
#             break
# # print(List)
# # リストの先頭からN個番目に'b'が何個あるかをカウントする
# print(List.count('b'))

n,a,b = map(int,input().split())

all = a+b
ans = 0
ans += n//all * a

if n%all > a:
    ans += a
else:
    ans += n % all

print(ans)