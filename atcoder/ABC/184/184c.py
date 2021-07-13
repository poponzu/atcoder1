# x1, y1 = map(int, input().split())
# x2, y2 = map(int, input().split())
#
#
# if x1+y1==x2+y2 or x1-y1 ==x2-y2 or abs(x1-x2)==abs(y1-y2):
#     print(0)
# else:
#     b1=y1-x1
#     b2=y2-x2
#     print(b1,b2)

r1, c1 = map(int, input().split())
r2, c2 = map(int, input().split())
r = r2 - r1
c = c2 - c1

if (r, c) == (0, 0):
    ans = 0

elif r == c or r == -c:
    ans = 1
elif abs(r) + abs(c) <= 3:
    ans = 1
elif (r ^ c ^ 1) & 1:
    ans = 2
elif abs(r) + abs(c) <= 6:
    ans = 2
elif abs(r + c) <= 3 or abs(r - c) <= 3:
    ans = 2
else:
    ans = 3

print(ans)

