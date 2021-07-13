# N = int(input())
# L = [list(map(int, input().split())) for i in range(N)]
#
# count =0
#
# for a in range(0,N):
#     for b in range(1,N):
#         for c in range(2,N):
#             dx1= L[b][0]-L[a][0]
#             dy1= L[b][1]-L[a][1]
#             dx2= L[c][0]-L[a][0]
#             dy2= L[c][1]-L[a][1]
#             if dx2*dy1==dx1*dy2:
#                 #print(a,b,c)
#                 if a==b or b==c or c==a:
#                     break
#                 print("Yes")
#                 exit()
# print("No")

n = int(input())
#p = [tuple(map(int, input().split())) for i in range(n)]

for i in range(n):
    for j in range(i):
            print(i,j)
