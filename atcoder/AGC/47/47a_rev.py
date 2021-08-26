S = input()
dict = {}
cur = ""
count = 0

for s in S:
    cur += s
    if cur not in dict.keys():
        count += 1
        dict ={}
        dict[cur] = 1
        cur = ""

print(count)
