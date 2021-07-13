x = input()
# print(x)
# print(len(x),x[0])
sum = 0
for i in range(len(x)):
    sum = sum + int(x[i])

if sum % 9 == 0:
    print('Yes')
else:
    print('No')