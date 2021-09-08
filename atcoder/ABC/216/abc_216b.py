from collections import Counter
N = int(input())
person = []
for _ in range(N):
    s,t = map(str,input().split())
    name = s + t
    person.append(name)

dict = Counter(person)

duplicate = False
for v in dict.values():
    if v >= 2:
        duplicate = True

if duplicate:
    print("Yes")
else:
    print("No")



# if len(person) == len(list(set(person))):
#     print("No")
# else:
#     print("Yes")
