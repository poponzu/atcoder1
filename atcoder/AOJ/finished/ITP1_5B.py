while(True):
    H, W = map(int, input().split())

    if H==0 and W==0:
        break
    print("#"*W)
    for i in range(1,H-1):
        print("#"+("."*(int(W)-2))+"#")
    print("#"*W)
    print()