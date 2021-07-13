N=int(input())

alpha=["z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y"]

q = N
ans = ""

while q!=0:
    if q%26 !=0:
        ans += alpha[q%26]
        q = q // 26
    else:
        ans += alpha[q%26]
        q = q // 26 - 1

print(ans[::-1])