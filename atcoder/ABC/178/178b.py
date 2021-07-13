a,b,c,d = map(int, input().split())

result= max(a*c,a*d)
result= max(result,b*c)
result= max(result,b*d)

print(result)