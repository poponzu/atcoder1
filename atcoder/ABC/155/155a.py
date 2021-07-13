a,b,c=map(int,input().split())

count = 0
if a==b:
    count = count + 1
if a == c:
    count = count + 1
if b == c:
    count = count + 1

if count == 1:
    print('Yes')
else:
    print('No')
