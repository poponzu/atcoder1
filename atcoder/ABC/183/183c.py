from itertools import permutations

city_list=[]
N,K=map(int,input().split())
T = [list(map(int, input().split())) for i in range(N)]

for city_number in range(2,N+1):
    city_list.append(city_number)

per=permutations(city_list,N-1)

count =0


for i in per:
    sum=0
    for p in range(len(i)-1):
        sum += T[i[p]-1][i[p+1]-1]

    sum += T[0][i[0]-1]+T[i[len(i)-1]-1][0]

    if sum==K:
        count+=1

print(count)




#print(T)



