h,a=map(int,input().split())
count = 0
result = h
for i in range(h):
    result = result - a
    count = count + 1
    if result <= 0:
        break

print(count)