from collections import deque
N,M,K=map(int,input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

desk_a = deque([])
desk_b = deque([])
for i in range(N-1,-1,-1):
    desk_a.append(A[i])

for j in range(M-1,-1,-1):
    desk_b.append(B[j])

time =0
ans=0

while True:
    # 二つとも空なら終了
    if len(desk_a) == 0 and len(desk_b) == 0:
        break

    #どっちも空でない場合
    if len(desk_a)!=0 and len(desk_b)!=0:
        pop_a= desk_a.pop()
        pop_b= desk_b.pop()

        #pop_aをtimeに足す
        if pop_a <= pop_b:
            time += pop_a
            if time <= K:
                ans +=1
                desk_b.append(pop_b)
            else:
                break

        #pop_bをtimeに足す
        elif pop_a > pop_b:
            time += pop_b
            if time <= K:
                ans+=1
                desk_a.append(pop_a)
            else:
                break



    # Aが空である場合
    if len(desk_a)==0 and len(desk_b)!=0:
        pop_b =desk_b.pop()
        time += pop_b
        if time <= K:
            ans+=1
        else:
            break


    # Bが空である場合
    if len(desk_a) !=0 and len(desk_b) == 0:
        pop_a = desk_a.pop()
        time += pop_a
        if time <= K:
            ans+=1
        else:
            break

print(ans)


