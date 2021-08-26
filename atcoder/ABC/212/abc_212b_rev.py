x = input()
same, step = True, True

for i in range(3):
    if int(x[i]) != int(x[i + 1]):
        same = False

    if int(x[i]) == 9:
        if int(x[i + 1]) != 0:
            step = False
    else:
        if int(x[i + 1]) != int(x[i]) + 1:
            step = False

if same or step:
    print("Weak")
else:
    print("Strong")
