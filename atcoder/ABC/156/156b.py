def Base_10_to_n(X, n):
    if (int(X / n)):
        return Base_10_to_n(int(X / n), n) + str(X % n)
    return str(X % n)


############################


#####関数をつかってみる．#####
######今回は二進数に変換######
# x10 = 35
# x2 = Base_10_to_n(x10, 2)
# print(x2)  # "100011"が表示される．def Base_10_to_n(X, n):
# print(len(x2))

n,k=map(int,input().split())
result = Base_10_to_n(n,k)
# print(result)
print(len(result))
# http://pixelbeat.jp/how_to_convert_n_ary_value_to_-decimal_and_decimal_to_n_ary/
#http://techtipshoge.blogspot.com/2010/05/10n.html
# http://iatlex.com/python/base_change#10n-2
# を参考にした
