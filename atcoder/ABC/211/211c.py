from collections import Counter

#S = input()
mod = 10**9 + 7
box = Counter("chokudai")

for i in box.values():
    i -= 1

print(box)