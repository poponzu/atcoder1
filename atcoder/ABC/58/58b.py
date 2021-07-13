O=input()
E=input()

ans =""
if len(O)==len(E):
    for i in range(len(O)):
        ans+=O[i]+E[i]
else:
    for j in range(len(E)):
        ans += O[j] + E[j]
    ans+= O[-1]

print(ans)