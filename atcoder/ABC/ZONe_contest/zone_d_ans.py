# from collections import deque
# s = deque()
# rev = False
# for i in input():
#     if i == 'R':
#         rev = not rev
#     elif rev:
#         if s and s[0] == i:
#             s.popleft()
#         else:
#             s.appendleft(i)
#     else:
#         if s and s[-1] == i:
#             s.pop()
#         else:
#             s.append(i)
#
# if rev:
#     s = reversed(s)
# print("".join(s))
#dequeはpop(left)とappend(left)の操作がO(1)なのがポイント
#dequeの計算量について載ってるhttps://qiita.com/Hironsan/items/68161ee16b1c9d7b25fb)

from collections import deque
s = deque()
rev = False
for i in input():
    if i == 'R':
        rev = not rev
    elif rev:
        if s and s[0] == i:
            s.popleft()
        else:
            s.appendleft(i)
    else:
        if s and s[-1] == i:
            s.pop()
        else:
            s.append(i)

if rev:
    s = reversed(s)
print("".join(s))