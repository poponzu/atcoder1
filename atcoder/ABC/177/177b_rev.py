S=input()
T=input()
#これはTの全通りを試せていない？
for i in range(len(T)):
    if S.find(T[:i+1])==-1:
        break

print(len(T)- i)