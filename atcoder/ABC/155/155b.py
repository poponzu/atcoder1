n = int(input())
List = list(map(int, input().split()))
denied_point = 0
List_even = [i for i in List if i % 2 == 0]

# print(List_even)
for i in List_even:
    if (i % 3) != 0 and (i%5 != 0):
        denied_point = denied_point + 1


if denied_point ==0 :
    print('APPROVED')
else:
    print('DENIED')





