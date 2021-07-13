W,H,X,Y = map(int,input().split())
#
# #右下
# if X == W and Y == 0:
#     print(W * H / 2, 0)
#     exit()
# #右上
# if X == W and Y == H:
#     print(W * H / 2 , 0)
#     exit()
# #左下
# if X == 0 and Y == 0:
#     print(W * H / 2, 0)
#     exit()
# #左上
# if X == 0 and Y == H:
#     print(W * H / 2, 0)
#     exit()

# #重心の場合は分割方法は二種類
# if X == W/2 and Y == H/2:
#     print(W * H / 2, 1)
#     exit()


# if Y == H/W * X or Y == (-H/W) * X + H:
#     print(W * H / 2, 0)
#     exit()

count = 0
if Y == H/W * X:
    count += 1

if Y == (-H/W) * X + H:
    count += 1

if count > 0:
    if count == 1:
        print(W * H / 2, 0)
        exit()
    else:
        print(W * H / 2, 1)
        exit()

lft = 0
rht = 0
horizon = 0

up = 0
down = 0
vertical = 0


#x = Xのとき
lft = X * H
rht = (W - X) * H
horizon = min(lft, rht)

# y = Yのとき
up = W * (H - Y)
down = W * Y
vertical = min(up, down)


ans1 = max(horizon, vertical)
# if horizon == vertical:
#     ans2 = 1
# else:
#     ans2 = 0
ans2 = 0

print(ans1, ans2)