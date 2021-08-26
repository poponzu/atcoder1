N = int(input())
alpha = ["a", "b", "c"]

def f(rest, s):
    if rest == 0:
        print(s)
    else:
        for c in alpha:
            f(rest - 1, s + c)


f(N, "")
