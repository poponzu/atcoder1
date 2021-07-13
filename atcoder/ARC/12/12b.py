N,v_person,v_turtle,distance=map(int,input().split())

for i in range(N):
    time=distance/v_person
    distance =time * v_turtle

# if distance<0.000001:
#     distance=0
print(distance)


