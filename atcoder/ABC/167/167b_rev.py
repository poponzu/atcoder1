A,B,C,K = map(int, input().split())

ans=0
count = K
if A>=K:
    ans += 1*count
    print(ans)
    exit()
elif A<K:
    count -= A
    ans += 1 * A
    if B >= count:
        ans += 0 * count
        print(ans)
        exit()
    elif B < count:
        count -= B
        ans += 0 * B
        if C>=count:
            ans += -1 * count
            print(ans)
            exit()
        elif C < count:
            ans += -1 * C
            print(ans)
            exit()