a, b, c = map(int, input().split())

count =0
if a!=b:
    for i in range(a,b+1):
        if c%i==0:
            count +=1
else:
    if c%a==0:
        count+=1

print(count)