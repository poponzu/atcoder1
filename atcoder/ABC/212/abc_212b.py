X = input()
count = [0] * 10

continus_count = 0
weak_flag = False

for i in range(1,4):
    if int(X[i]) == 0:
        if int(X[i-1]) == 9:
            continus_count += 1
    else:
        if int(X[i]) == int(X[i-1]) + 1:
            continus_count += 1

if continus_count == 3:
    weak_flag = True

# すべて同じ数字かどうか
for x in X:
    count[int(x)] += 1

if 4 in count:
    weak_flag = True

if weak_flag:
    print("Weak")
else:
    print("Strong")
