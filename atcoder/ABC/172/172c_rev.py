import itertools
import operator
import bisect

N, N, K = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

Aread = [0] + list(itertools.accumulate(A))
Bread = [0] + list(itertools.accumulate(B))

all_num_book = 0
B_num_book = 0
Max = 0

for i in range(1,N):
        B_num_book = bisect.bisect_right(Bread,K-Aread[i]) - 1
        if B_num_book != -1:
            all_num_book = i + B_num_book
            Max = max(all_num_book, Max)
print(Max)