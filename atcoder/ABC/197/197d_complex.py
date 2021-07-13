import math

N = int(input())
x0, y0 = map(int, input().split())
X, Y = map(int, input().split())
#中点取得
Cx = (x0 + X) / 2
Cy = (y0 + Y) / 2

rad = math.radians(360/N)

p1= complex(x0,y0)
p3= complex(Cx,Cy)
rot=complex(math.cos(rad),math.sin(rad))

#点p1を点p3の周りに角radだけ回転させる
ans=(p1-p3)*rot+p3

print(ans.real,ans.imag,end=' ')

