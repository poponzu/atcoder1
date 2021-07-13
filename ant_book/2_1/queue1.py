# q = []
# q.append(1)  # [1]
# q.append(2)  # [1, 2]
# q.append(3)  # [1, 2, 3]
# q.pop(0)     # 一番下から取り除く [1, 2, 3] -> [2, 3]
# q.append(4)
# print(q)
# q.pop(0)     # [2, 3] -> [3]
#
# q.pop(0)     # [3] -> []

from collections import deque

q = deque([])
q.append(1)  # [1]
q.append(2)  # [1, 2]
q.append(3)  # [1, 2, 3]
q.popleft()  # 一番下から取り除く [1, 2, 3] -> [2, 3]
q.popleft()  # [2, 3] -> [3]
q.popleft()  # [3] -> []