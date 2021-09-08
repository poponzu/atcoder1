# 解法1
import itertools

num = list(map(int,input().split()))
tot = []

comb = itertools.combinations(range(5),3)

for pair in comb:
    c_sum = 0
    for i in pair:
        c_sum += num[i]
    tot.append(c_sum)

tot.sort()

print(tot[-3])



# 解法2
num = list(map(int,input().split()))

num.sort()

# a,b,c,d,eという昇順シートされた列があるとき、この中から三つ選んでその和を考える
# その全ての組み合わせの和で３番目に多いのは,a+d+e かb+c+eの大きい方
# b+c+eに気づけなかった
print(max(num[-1] + num[-2] + num[0],num[1] + num[2] + num[4]))

