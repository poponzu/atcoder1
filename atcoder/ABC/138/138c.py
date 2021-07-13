#12分AC

#分母が大きいものは、なるべく小さい数にあてるのがいい
#ユーザ解説の方がわかりやすい
N = int(input())
V =list(map(int,input().split()))

V = sorted(V)

for i in range(N-1):
    value = (V[i]+V[i+1])/2
    V[i+1] = value

print(V[-1])