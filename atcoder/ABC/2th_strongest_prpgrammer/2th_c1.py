A, B = map(int, input().split())

gcd_max=1
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

if A*2<=B:
    for a in range(A,B//2+1):
        for b in (B//2,B+1):
            current_gcd=gcd(a,b)
            if gcd_max<current_gcd:
                gcd_max=current_gcd
else:
    for a in range(A,A+((B-A)//2+1)):
        for b in range(a+1,B+1):
            current_gcd=gcd(a,b)
            if gcd_max<current_gcd:
                gcd_max=current_gcd

print(gcd_max)

