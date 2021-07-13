while(True):
    m, f, r = map(int, input().split())
    goukei = m + f

    if m==-1 and f==-1 and r==-1:
        exit()
    elif m==-1 or f == -1:
        print("F")
    elif goukei >=80:
        print("A")
    elif 65 <= goukei < 80:
        print("B")
    elif 50 <= goukei < 65:
        print("C")
    elif 30 <= goukei < 50:
        if r >= 50:
            print("C")
        else:
            print("D")
    else:
        print("F")

# #if文だけだと　うまいこと抜けれない
# #これは不正解
#
# while(True):
#     m, f, r = map(int, input().split())
#     goukei = m + f
#
#     if m==-1 and f==-1 and r==-1:
#         exit()
#     if m==-1 or f == -1:
#         print("F")
#     if goukei >=80:
#         print("A")
#     if 65 <= goukei < 80:
#         print("B")
#     if 50 <= goukei < 65:
#         print("C")
#     if 30 <= goukei < 50:
#         if r >= 50:
#             print("C")
#         else:
#             print("D")
#     if goukei < 30:
#         print("F")




