N=int(input())

count =0
for a in range(1,10**6+1):
    if N%a==0:
        count +=(N//a) - 1
    else:
        count +=N//a

print(count)

