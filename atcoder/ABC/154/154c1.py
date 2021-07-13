
#TLEやった
# オーダを少なくする
def has_duplicates(seq):
    return len(seq) != len(set(seq))

n =int(input())
List=list(map(int,input().split()))
if has_duplicates(List) == False:
    print('YES')
else:
    print("NO")