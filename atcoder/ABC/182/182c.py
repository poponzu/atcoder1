N=input()
r=[0,0,0]

for n in N:
    n=int(n)
    if n%3==0:
        r[0] += 1
    elif n%3==1:
        r[1] += 1
    else:
        r[2] += 1

sum=(0*r[0])+(1*r[1])+(2*r[2])
N=str(N)

if sum % 3==0:
    print("0")
elif sum %3==1:
    if r[1]>=1:
        if len(N)!=1:
            print("1")
        else:
            print("-1")
    else:
        if r[2]>=2:
            if len(N)!=2 and len(N)!=1:
                print("2")
            else:
                print("-1")
else:
    if r[2]>=1:
        if len(N)!=1:
            print("1")
        else:
            print("-1")
    else:
        if r[1]>=2:
            if len(N)!=2 and len(N)!=1:
                print("2")
            else:
                print("-1")
        else:
            print("-1")
