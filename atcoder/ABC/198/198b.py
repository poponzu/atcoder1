N=input()

zero_count=N.count('0')

if N==N[::-1]:
    #777などの回文の時
    print('Yes')
    exit()

if zero_count >0:
    new_N = '0'*zero_count+N
    if new_N == new_N[::-1]:
        print('Yes')
        exit()

print('No')


