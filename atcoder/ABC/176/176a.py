# N,X,T = map(int, input().split())
#
# answer = 0
#
# if N%X == 0:
#     S = int(N/X)
#     answer = S*T
# else:
#     S = int(N / X)
#     answer = (S+1) * T
#
# print(int(answer))

def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]

def even_odd_count_of_divisors(n):
    even = 0
    odd = 0
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            #lower_divisors.append(i)
            if i % 2 == 0:
                even += 1
            else:
                odd += 1

            if i != n // i:
                #upper_divisors.append(n//i)
                if n//i % 2 == 0:
                    even += 1
                else:
                    odd += 1
        i += 1
    if even == odd:
        return('Same')
    elif even > odd:
        return('Even')
    else:
        return('Odd')

#全探索以外わからない
for i in range(1,51):
    print(str(i)+'は'+str(make_divisors(i))+'で'+str(even_odd_count_of_divisors(i)))