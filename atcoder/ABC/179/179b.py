N = int(input())
D = [list(map(int, input().split())) for i in range(N)]

seq_count =0

for i in range(N):
    if D[i][0] ==D[i][1]:
        seq_count += 1
    else:
        seq_count =0
    if seq_count==3:
        print("Yes")
        exit()
print("No")
