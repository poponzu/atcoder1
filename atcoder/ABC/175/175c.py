x,k,d = map(int,input().split())

right = 0
left = 0

if x % d == 0:
    left = 0
    right = left + d
    if x<0:
        left,right = right,left
    # このrightに辿りついたなら
    if k >= (x - right) // d:
        rest = k - (x - right) // d
        if rest % 2 == 0:
            ans = abs(right)
        else:
            ans = abs(left)
    else:
        ans = x - (k * d)
else:
    left = x -(x//d + 1) * d
    right = left + d
    if x<0:
        left,right = right,left
    #このrightに辿りついたなら
    if k >= (x- right)//d:
        rest = k - (x - right)//d
        if rest % 2==0:
            ans = abs(right)
        else:
            ans = abs(left)
    else:
        ans = x - (k * d)

print(ans)