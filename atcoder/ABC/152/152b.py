a,b=map(int,input().split())
stra = str(a) * b
# print(int(stra))
strb = str(b) * a
if stra<=strb:
    print(int(stra))
else:
    print(int(strb))