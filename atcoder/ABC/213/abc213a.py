a,b = map(int,input().split())
# 解法1(全探索）
# for c in range(256):
#     if a ^ c == b:
#         print(c)
#         exit()

# 解法2(両辺にxorを施す）
print(b ^ a)