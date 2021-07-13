# # スタック
# s = []
#
# s.append(1)  # [1]
# s.append(2)  # [1, 2]
# s.append(3)  # [1, 2, 3]
# s.pop()      # 一番上から取り除く [1, 2, 3] -> [1, 2]
# print(s)
# s.pop()      # [1, 2] -> [1]
# print(s)
# s.pop()      # [1] -> []
# print(s)

from collections import deque

s = deque([])
s.append(1)  # [1]
s.append(2)  # [1, 2]
s.append(3)  # [1, 2, 3]
s.pop()      # 一番上から取り除く [1, 2, 3] -> [1, 2]
print(s)
s.pop()      # [1, 2] -> [1]
s.pop()      # [1] -> []