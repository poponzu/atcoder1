a = [0] * 21

a[1] = 100
a[2] = 100
a[3] = 200

for n in range(4,21):
    a[n] = a[n-1] + a[n-2] + a[n-3]

print(a[20])