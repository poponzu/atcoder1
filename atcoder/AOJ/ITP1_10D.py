n = int(input())
x = list(map(float, input().split()))
y = list(map(float, input().split()))

D_xy1 =0
for i in range(n):
    D_xy1 += abs(x[i]-y[i])
print(D_xy1**(1/1))

D_xy2 =0
for i in range(n):
    D_xy2 += abs(x[i]-y[i])**2
print(D_xy2**(1/2))

D_xy3 =0
for i in range(n):
    D_xy3 += abs(x[i]-y[i])**3
print(D_xy3**(1/3))

D_xy4 =0
max_value = abs(x[0]-y[0])
for i in range(1,n):
     max_value = max(abs(x[i]-y[i]),max_value)
print(max_value)