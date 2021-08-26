# import math
N = int(input())
# print(math.log(3**8,10))
alpha = ["a", "b", "c"]
ans = ""
if N == 1:
    for i in range(3):
        ans += alpha[i]
        print(ans)
        ans = ""
elif N == 2:
    for i in range(3):
        for j in range(3):
            ans += alpha[i]
            ans += alpha[j]
            print(ans)
            ans = ""
elif N == 3:
    for i in range(3):
        for j in range(3):
            for k in range(3):
                ans += alpha[i]
                ans += alpha[j]
                ans += alpha[k]
                print(ans)
                ans = ""
elif N == 4:
    for i in range(3):
        for j in range(3):
            for k in range(3):
                for l in range(3):
                    ans += alpha[i]
                    ans += alpha[j]
                    ans += alpha[k]
                    ans += alpha[l]
                    print(ans)
                    ans = ""
elif N == 5:
    for i in range(3):
        for j in range(3):
            for k in range(3):
                for l in range(3):
                    for m in range(3):
                        ans += alpha[i]
                        ans += alpha[j]
                        ans += alpha[k]
                        ans += alpha[l]
                        ans += alpha[m]
                        print(ans)
                        ans = ""
elif N == 6:
    for i in range(3):
        for j in range(3):
            for k in range(3):
                for l in range(3):
                    for m in range(3):
                        for n in range(3):
                            ans += alpha[i]
                            ans += alpha[j]
                            ans += alpha[k]
                            ans += alpha[l]
                            ans += alpha[m]
                            ans += alpha[n]
                            print(ans)
                            ans = ""
elif N == 7:
    for i in range(3):
        for j in range(3):
            for k in range(3):
                for l in range(3):
                    for m in range(3):
                        for n in range(3):
                            for o in range(3):
                                ans += alpha[i]
                                ans += alpha[j]
                                ans += alpha[k]
                                ans += alpha[l]
                                ans += alpha[m]
                                ans += alpha[n]
                                ans += alpha[o]
                                print(ans)
                                ans = ""
elif N == 8:
    for i in range(3):
        for j in range(3):
            for k in range(3):
                for l in range(3):
                    for m in range(3):
                        for n in range(3):
                            for o in range(3):
                                for p in range(3):
                                    ans += alpha[i]
                                    ans += alpha[j]
                                    ans += alpha[k]
                                    ans += alpha[l]
                                    ans += alpha[m]
                                    ans += alpha[n]
                                    ans += alpha[o]
                                    ans += alpha[p]
                                    print(ans)
                                    ans = ""