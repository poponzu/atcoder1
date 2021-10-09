from collections import Counter

text = input("Type a word.")

dict = Counter(text)

# print(dict)

# dict2 = sorted(dict.items())
# print(sorted(dict2))


for alpha,count in dict.items():
    ans = []
    for i in range(count):
        ans.append(alpha)
    print("'" + alpha + "': ",end="")
    print(ans)