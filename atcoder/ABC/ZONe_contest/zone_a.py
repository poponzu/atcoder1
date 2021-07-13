S=input()
ans="ZONe"
count=0
for i in range(11):
    if ans==S[i:i+4]:
        count +=1
print(count)