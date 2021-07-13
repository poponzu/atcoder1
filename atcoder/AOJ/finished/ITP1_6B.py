N = int(input())
have_t = [list(map(str, input().split())) for i in range(N)]

perfect_t=[]
pattern=["S","H","C","D"]

#欠けていないトランプのリストを作成
for pattern in pattern:
    for i in range(1,14):
        add_t =[pattern,str(i)]
        perfect_t.append(add_t)

#in を使わない書き方
# print(perfect_t)
# for p in perfect_t:
#     match =0
#     for i in  range(N):
#         if p == have_t[i]:
#             match +=1
#     if match ==0:
#         print(*p)

for p in perfect_t:
    if p not in have_t:
        print(*p)





