n = 3

map_ = {}

for c in range(1, n + 1):
    for d in range(1, n + 1):
        result = c ** 3 + d ** 3
        map_.setdefault(result, [c, d])

# print(map_)

for a in range(1, n + 1):
    for b in range(1, n + 1):
        result = a ** 3 + b ** 3
        # map_の辞書からキーで検索してバリューを取得したい。
        list = map_.get(result)
        print(a,b,list)
        # for pair in list:
        #     print(a,b,pair)
