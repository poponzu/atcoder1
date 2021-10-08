# 8:27 ~

T = int(input())
for _ in range(T):
    ans = 0
    n2, n3, n4 = map(int,input().split())

    # O(10**4)以下で10の棒が何個作れるかを出力する
    for n2 in range(5):
        for n3 in range(4):
            for n4 in range(3):
                if (2 * n2 + 3 * n3 + 4 * n4 ==10) and (n2 == 0 or n3 == 0 or n4 == 0):
                    print(n2,n3,n4)
                    ans += 1
    print(ans)