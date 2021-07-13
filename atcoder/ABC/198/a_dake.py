N,x=map(int,input().split())
a=list(map(int,input().split()))
ans =0

for i in range(2**N):
    glad_num =0
    for j in range(N):  # このループが一番のポイント
        if ((i >> j) & 1):  # 順に右にシフトさせ最下位bitのチェックを行う
            if x>a[j]:
                x = x - a[j]
    ans =max(glad_num,ans)

print(ans)

# #
# if x > a[j]:
#     glad_num += 1
#     x = x - a[j]