from collections import deque
S=input()
d=deque()

rev = False

for s in S:
    if s=="R":
        rev= not rev
    else:
        if rev:
            if d and d[-1]==s:
                d.pop()
            else:
                d.append(s)
        else:
            if d and d[0]==s:
                d.popleft()
            else:
                d.appendleft(s)


if rev==False:
    d=reversed(d)

print("".join(d))




