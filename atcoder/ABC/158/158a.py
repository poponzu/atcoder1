# a,b,c=input()
# # print(a,b,c)
# List = []
# List.append(a)
# List.append(b)
# List.append(c)
# # print(List)
# for i in range(0,2):
#     if List[i] != List[i + 1]:
#         print('Yes')
#         exit()
#
# print('No')
S=input()

if S[0]==S[1] and S[1]== S[2] and S[2] == S[0]:
    print("No")
else:
    print("Yes")