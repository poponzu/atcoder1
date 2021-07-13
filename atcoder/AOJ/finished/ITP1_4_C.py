while(True):
    a,op,b = input().split()
    a = int(a)
    b = int(b)

    if op =="?":
        break

    if op=="+":
        print(a+b)
    if op=="-":
        print(a-b)
    if op=="*":
        print(a*b)
    if op=="/":
        if a%b !=0:
            print(int(a//b))
        else:
            print(int(a/b))

