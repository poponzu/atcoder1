import itertools

N = int(input())
L = list(map(int, input().split()))
count = 0

def has_duplicates(seq):
    return len(seq) != len(set(seq))


for pair in itertools.combinations(L, 3):
    # print(list(pair))
    if has_duplicates(pair) == False:

        if (pair[0] + pair[1] > pair[2]) and (pair[1] + pair[2]) > pair[0] \
                and (pair[2] + pair[0] > pair[1]):
            count += 1





print(count)
