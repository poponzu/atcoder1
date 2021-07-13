#H, W = map(int, input().split())
# Ch, Cw = map(int, input().split())
#
# Dh, Dw = map(int, input().split())
#
# S = [input() for i in range(H)] #複数行の数値の入力を取得
#
# # print(S[0][0],S[1][2]) #出力：['s_1', 's_2', 's_3', 's_N']
#
# print(H,W)
# print(Ch,Cw)
# print(Dh,Dw)
# print(S)
#
# # コードに写せない

T = int(input())

X = [int(input()) for i in range(T)]

#計算量O(ルートN)
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

for i in X:
    print(even_odd_count_of_divisors(i))


