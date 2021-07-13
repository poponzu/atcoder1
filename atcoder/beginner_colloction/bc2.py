A=int(input())
B=int(input())
C=int(input())


if A==max(A,B,C):
    if B==max(B,C):
        print(1)
        print(2)
        print(3)
    else:
        print(1)
        print(3)
        print(2)
elif B==max(A,B,C):
    if A==max(A,C):
        print(2)
        print(1)
        print(3)
    else:
        print(3)
        print(1)
        print(2)
elif C==max(A,B,C):
    if A==max(A,B):
        print(2)
        print(3)
        print(1)
    else:
        print(3)
        print(2)
        print(1)