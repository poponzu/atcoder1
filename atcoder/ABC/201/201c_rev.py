S=input()

o=[]
x=[]
for number,s in enumerate(S):
    if s=="o":
        o.append(str(number))
    elif s=="x":
        x.append(str(number))

count = 0
for i in range(10000):
    flag = True
    #パスワード生成
    i=str(i)
    passward="0"*(4-len(i))+i

    #xのlistの要素が一つも含まれてはいけない
    # if all(dame not in passward for dame in x)==False:
    #     flag=False
    for p in passward:
        if p in x:
            flag = False

    #oのlistの要素の全てがpasswardに含まれていなければならない
    if all(c in passward for c in o)==False:
        flag=False

    if flag==True:
        count +=1

print(count)







