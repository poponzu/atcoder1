import sys
input = sys.stdin.readline
import re

S=input()

for i in range(len(S)//2+1):
    S=re.sub("([a-z])\\1(?!\\1)", "", S)


T=[],
for s in S:
    if s=="R":
        T=T[::-1]
    else:
        T+=s

for t in range(len(T)//2+1):
    T=re.sub("([a-z])\\1(?!\\1)", "", T)

print(T)

