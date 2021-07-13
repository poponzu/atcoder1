counter=[0]*10000
alpha = [chr(i) for i in range(97, 97+26)]

while True:
    try:
        ch = input()
        for w in ch:
            num = ord(w.lower()) - ord('a')  # 文字 ch の番号num = ord(ch) - ord('a')   # 文字 ch の番号
            counter[num] += 1  # 文字 ch をカウント

    except EOFError:
        break

for i in range(26):
        print(alpha[i] + " : " + str(counter[i]))

