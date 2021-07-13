n = int(input())
p =[tuple(map(int,input().split()))for i in range(n)]

for i in range(n):
    for j in range(i):
        for k in range(j):
            x1,y1 = p[i]
            x2,y2 = p[j]
            x3,y3 = p[k]

            x1_new = x2-x1
            y1_new = y2-y1
            x2_new = x3-x1
            y2_new = y3-y1

            if x1_new * y2_new == x2_new * y1_new:
                #print(p[i],p[j],p[k])
                print("Yes")
                exit()
print("No")