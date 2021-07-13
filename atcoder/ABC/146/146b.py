N=int(input())
S=input()
alphabets = [chr(i) for i in range(65, 65+26)]

for i in S:
    print(alphabets[(alphabets.index(i)+N)%26],end ="")
print()

