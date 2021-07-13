S = int(input())

hour = S//3600
minute= (S%3600)//60
second = (S%3600)%60

print(str(hour)+":"+str(minute)+":"+str(second))
