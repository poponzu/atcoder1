s,t=input().split()
# print(s,t)
ns,nt=map(int,input().split())
# print(ns,nt)
judge = input()
# print(judge)
if s == judge:
    ns = ns-1
elif t == judge:
    nt = nt -1
print(ns,nt)
