n = 10

map_ = {}

for c in range(1, n + 1):
    for d in range(1, n + 1):
        result = c ** 3 + d ** 3
        map_.setdefault(result, [[c, d]])

for result,list in map_.items():
    # listを二次元配列扱いにしたい
    # 8行目を二次元リストに変えた
    for pair1 in list:
        for pair2 in list:
            print(pair1[0],pair1[1],pair2[0],pair2[1])
            print("--------")