A1,A2,A3=map(int,input().split())

if A2-A1==A3-A2:
    print("Yes")
    exit()
elif A3-A1==A2-A3:
    print("Yes")
    exit()
elif A1-A2==A3-A1:
    print("Yes")
    exit()
elif A3-A2==A1-A3:
    print("Yes")
    exit()
elif A1-A3==A2-A1:
    print("Yes")
    exit()
elif A2-A3==A1-A2:
    print("Yes")
    exit()

print("No")