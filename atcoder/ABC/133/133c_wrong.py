L,R = map(int,input().split())

L_count = L // 2019
R_count = R // 2019

L= L%2019
R= R%2019

ans = 0
mod = 2019
if L < R:
    if L_count < R_count:
        ans = 0
    else:
        ans =(L * (L+1))%2019
elif L > R:
    ans = 0
else:
    ans = 0

print(ans)





