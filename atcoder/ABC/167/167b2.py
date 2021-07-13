A,B,C,K = map(int, input().split())

card=[]
for a in range(A):
    card.append(1)
for b in range(B):
    card.append(0)
for c in range(C):
    card.append(-1)

print(sum(card[:K]))