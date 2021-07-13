from itertools import permutations

N=int(input())
P=tuple(map(int,input().split()))
Q=tuple(map(int,input().split()))

table=[]
for i in range(N):
    table.append(i+1)


P_index= 0
Q_index= 0
per=list(permutations(table,N))

P_index=per.index(P)+1
Q_index=per.index(Q)+1

print(abs(P_index-Q_index))



