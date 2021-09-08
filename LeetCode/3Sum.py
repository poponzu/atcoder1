import itertools

# 標準ライブラリにある変数を新しく定義しない。
# 二分探索使うときはソートされている必要がある。

class Solution:
    def threeSum(self, nums):
        nums.sort()
        if len(nums) <= 2:
            return []

        target = range(len(nums))
        ans = []
        for i, comb in enumerate(itertools.combinations(target, 2)):
            sum = 0
            for j in comb:
                sum += nums[j]
            need = -sum
            index = binarySearch(nums, need)
            # 三つ目の要素がみつかったらその三つの要素全てを記録
            if index != -1 and index != comb[0] and index != comb[1]:
                ans.append(sorted([nums[comb[0]], nums[comb[1]], nums[index]]))

        ans = list(map(list, set(map(tuple, ans))))
        return ans


# 二分探索
def binarySearch(a, x):
    low = 0
    high = len(a) - 1
    mid = 0

    while low <= high:
        # ここ切り捨ての//でいいのかどうか
        mid = (low + high) // 2
        if a[mid] < x:
            low = mid + 1
        elif a[mid] > x:
            high = mid - 1
        else:
            return mid

    return -1  # エラー


question = [-1,0,1,2,-1,-4,-2,-3,3,0,4]
a = Solution()
print(a.threeSum(question))
