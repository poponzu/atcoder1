N=int(input())

count = 0
#これってO(N**2)じゃないの？

for i in range(1,N+1):
    if "7" not in str(i) and "7" not in oct(i):
        count+=1

print(count)