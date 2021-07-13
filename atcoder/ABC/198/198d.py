# s1 = input()
# s2 = input()
# s3 = input()
#
# flag1 = 1
# flag2 = 1
# flag3 = 1
#
# for x in range(1,len(s1)+1):
#     for y in range(1,len(s2)+1):
#             z = x+y
#             if len(str(x))==len(s1) and len(str(y))== len(s2) and len(str(z))== len(s3):
#                 flag1 =1
#             if z >0:
#                 flag2 =1


#三つ目の条件が実装できない
#二次元要素で?行2列の行列を返したらいいのはわかる。
def common(s1,s2):
    common_index=[]
    for i in len(s1):
        for j in len(s2):
            if s1[i] == s2[j]:
                common_index.append([i,j])

    return common_index

print(common("ca","ab"))