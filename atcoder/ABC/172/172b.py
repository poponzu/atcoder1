data =[96,54,52,48]

line =[150,150,100,100]
row =[148,102,148,102]

data_sum = sum(data)
# print(data_sum)

# 期待値のリスト作成
# expect=[(line[0]*row[0])/data_sum,(line[1]*row[1])/data_sum,
#         (line[2]*row[2])/data_sum,(line[3]*row[3])/data_sum]

expect=[0,0,0,0]
for i in range(0,4):
    expect[i]= (line[i]*row[i])/data_sum

print(expect)

# カイ二乗のリスト作成
# Chi_square=[pow(data[0]-expect[0],2)/expect[0],pow(data[1]-expect[1],2)/expect[1],
#             pow(data[2]-expect[2],2)/expect[2],pow(data[3]-expect[3],2)/expect[3]]

Chi_square =[0,0,0,0]

for j in range(0,4):
    Chi_square[j]= pow(data[j]-expect[j],2)/expect[j]

print(Chi_square)

# カイ二乗の値を求める
print(sum(Chi_square))

# print(pow(data[0]-expect[0],2)/expect[0])
