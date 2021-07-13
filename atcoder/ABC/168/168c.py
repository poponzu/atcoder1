import math


def int_sqrt2(n):
    def f(prev):
        while True:
            m = (prev + n / prev) / 2
            if m >= prev:
                return prev
            prev = m

    return f(int(math.sqrt(n) * (1 + 1e-10)))


a, b, hour, minute = map(int, input().split())
ang= 0

# 例外処理
if hour == 0 and minute ==0:
    print(0)
    exit()
# 短針の角度取得
rShort = (hour * (360 / 12)) + minute * 1/2;
# 長針の角度取得
rLong = minute * (360 / 60);
# 角度取得
ang = abs(rLong - rShort);
# 適切な角度取得
ang = min(ang, (360 - ang));

if ang == 90:
    print(int_sqrt2(a*a + b*b))
elif ang == 180:
    print(a+b);
else:
   c2 = a*a+ b*b -2*a*b*math.cos(ang);
   c = int_sqrt2(c2);
   print(c)
   print(math.cos(ang))
   print(math.cos(80))