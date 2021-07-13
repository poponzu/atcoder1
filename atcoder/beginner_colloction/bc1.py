N=int(input())
T=[0]
X=[0]
Y=[0]

for i in  range(N):
    t,x,y =list(map(int,input().split()))
    T.append(t)
    X.append(x)
    Y.append(y)

count =0
for i in range(0,N):
    can =True
    dt =T[i+1]-T[i]
    dist=abs(X[i]-X[i+1])+abs(Y[i]-Y[i+1])

    if dt < dist:
        can = False
    if dist%2!=dt%2:
        can=False

if can == True:
    print("Yes")
else:
    print("No")


