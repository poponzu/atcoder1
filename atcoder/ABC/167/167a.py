List = [input() for i in range(2)]
S = List[0]
T = List[1]
# print(S)
# print(T)
if S==T[:-1]:
    print('Yes')
else:
    print('No')