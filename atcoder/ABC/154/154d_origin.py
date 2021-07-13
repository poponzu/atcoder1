N, K = map(int, input().split())
# print(N,K)
p = list(map(int, input().split()))
# print(p)
# 1 から P までの P 種類の目が等確率で出るサイコロの出目の期待値は (1 + P)/2 です。
p_exp = [(1+i)/2 for i in p]
# print('期待値が入ったリストp')
# print('p='+ str(p_exp))
# 期待値が入ったリストpができた
# 新たに累積和リストSを作成する
S =[0] * N
S[0] = p_exp[0]
for i in range(len(p_exp) - 1):
    S[i + 1] = S[i] + p_exp[i + 1]
# print('累積和が入ったリスト')
# print('S=' + str(S))
S.insert(0, 0)
# print('累積和が入ったリストに先頭0挿入したリスト')
# print('S=' + str(S))
max =0
exp_sum = 0
for j in range(N - K + 1):
    exp_sum = S[j + K] - S[j]
    if max < exp_sum:
        max = exp_sum
# print('求める最大値maxは')
# print('max=' + str(max))
print(max)