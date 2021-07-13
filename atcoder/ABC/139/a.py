String1 = input()
String2 = input()
count = 0
for i in range(0, 3):
    if String1[i] == String2[i]:
        count = count + 1

print(count)
