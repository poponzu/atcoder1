while True:
    n,x = map(int,input().split())

    if n==0 and x==0:
        break

    num = []
    for i in range(1, n + 1):
        num.append(i)

    count=0

    for i in range(n):
        for j in range(i):
            for k in range(j):
                if num[i]+num[j]+num[k]==x:
                    count +=1

    print(count)


#split()についてしらべただけ
# s_blank = 'one two     three\nfour\tfive'
# print(s_blank)
# print(s_blank.split())