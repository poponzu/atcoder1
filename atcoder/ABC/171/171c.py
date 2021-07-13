import string
A =string.ascii_lowercase
alpha_list=list(A)

N = int(input())

def send_alpha(x):
    return alpha_list[x-1]

# 桁数を決める
digit = 1
alpha_count = 26
for i in range(0,12):
    if N < alpha_count:
        digit = i +1
        break
    else:
        alpha_count *= alpha_count

# print(digit)

