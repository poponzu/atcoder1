words=input().upper()
text=[]

while(True):
    tmp_text = str(input())
    if tmp_text=="END_OF_TEXT":
        break
    text += tmp_text.upper().split()


# print(words,text)

ans = 0

for t in text:
    if t==words:
        ans += 1

print(ans)