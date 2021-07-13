while(True):
    H, W = map(int, input().split())

    if H==0 and W==0:
        break
    for h in range(H):
        #偶数行
        if h%2 ==0:
            for w in range(W):
                if w == W-1:
                    if w % 2 == 0:
                        print("#")
                        break
                    else:
                        print(".")
                        break
                if w%2==0:
                    print("#",end="")
                else:
                    print(".",end="")

        #奇数行
        else:
            for w in range(W):
                if w == W-1:
                    if w % 2 == 0:
                        print(".")
                        break
                    else:
                        print("#")
                        break
                if w % 2 == 0:
                    print(".",end="")
                else:
                    print("#",end="")
    print()
