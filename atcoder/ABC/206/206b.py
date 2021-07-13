N = int(input())

for i in range(1,10**6):
    money = i*(i+1)*0.5
    if N <= money:
        print(i)
        exit()

