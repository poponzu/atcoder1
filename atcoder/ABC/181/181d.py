S =input()
flag1 =0
flag2 =0

#２の倍数かどうか0(len(N)) ok
for i in range(len(S)):
    if int(S[i])%2 ==0:
        flag1 =1

#4の倍数かどうかlen(S）が1の時だけ場合わけ
if len(S)!=1:
    for a in range(len(S)):
        for b in range(1,len(S)):
            if a==b:
                break
            if int(str(a)+str(b))%4 ==0:
                flag2=1
else:
    if int(S)%4 ==0:
        flag2 = 1

if flag1==1 and flag2 ==1:
    print("Yes")
else:
    print("No")