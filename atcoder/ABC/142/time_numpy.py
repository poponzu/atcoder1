import numpy as np
import time

N = int(input())
A = list(map(int,input().split()))
A = np.array(A)

start = time.time()
print(*(A.argsort()))
process_time = time.time() - start

print("実行時間: "+str(process_time))