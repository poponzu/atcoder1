from operator import itemgetter
import time

N = int(input())
A = list(map(int, input().split()))

start = time.time()
print(*[t[0] for t in sorted(enumerate(A), key=itemgetter(1))])
process_time = time.time() - start
print("実行時間: "+str(process_time))
