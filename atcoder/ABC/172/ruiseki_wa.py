import itertools

A=[2,4,6,8,10]
#S1はaccumulate使わず
S1 =[0]
for i in range(len(A)):
    sum = S1[i] + A[i]
    S1.append(sum)

#S2はaccumulate使う
S2 = [0] + list(itertools.accumulate(A))

print("S1は" + str(S1)) #S1は[0, 2, 6, 12, 20, 30]
print("S2は" + str(S2)) #S2は[0, 2, 6, 12, 20, 30]

#使いやすい