N = int(input())

# person = []
# for _ in range(N):
#     s,t = map(str,input().split())
#     name = s + t
#     person.append(name)

person = [input() for _ in range(N)]


if len(set(person)) < N:
    print("Yes")
else:
    print("No")
