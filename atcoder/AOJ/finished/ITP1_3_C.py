for i in range(3000):
    x, y = map(int, input().split())

    if x ==0 and y==0:
        break
    if x>y:
        # swap = x
        # x = y
        # y = swap
        x,y = y,x

    print(x,y)