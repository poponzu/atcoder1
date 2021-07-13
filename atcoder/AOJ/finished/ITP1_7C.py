r,c = map(int,input().split())
x = [list(map(int, input().split())) for i in range(r)]

#行合計を元のリストに追加
for line1 in range(r):
    sum1 = 0
    for column1 in range(c):
        sum1 += x[line1][column1]
    x[line1].append(sum1)

#列に対する合計を新しくcolumnリストに追加
column =[]
for column2 in range(c):
    sum2= 0
    for line2 in range(r):
        sum2 += x[line2][column2]
    column.append(sum2)

#columnリストに一番右下を追加
column.append(sum(column))
#columnを元のリストと合体
x.append(column)

#出力
for ans in x:
    print(*ans)


