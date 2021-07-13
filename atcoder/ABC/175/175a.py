x = input()
count = 0
if x[0] == 'S':
    if x[1] == 'R':
        count+= 1
        if x[2] == 'R':
            count += 1
        if x[2] == 'S':
            count = count

    if x[1] == 'S':
        if x[2] == 'R':
            count += 1
        if x[2] == 'S':
            count = count

if x[0] == 'R':
    count += 1
    if x[1] == 'R':
        count+= 1
        if x[2] == 'R':
            count += 1
        if x[2] == 'S':
            count = count

    if x[1] == 'S':
        if x[2] == 'R':
            count = 1
        if x[2] == 'S':
            count = count

print(count)