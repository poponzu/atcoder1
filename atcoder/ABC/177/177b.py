S=input()
T=input()

ans =int(len(T))

#iはSの何文字目から重ねる位置を示す
for start in range(len(S)-len(T)+1):
    diff=0
    for i in range(len(T)):
        if T[i]!=S[start + i]:
            diff+= 1
    #minは小さい方をとる
    ans = min(ans,diff)

print(ans)

