from collections import Counter


class Solution:
    def singleNumber1(self, nums):
        dict = Counter(nums)
        for k, v in dict.items():
            if v == 1:
                print(k)
                return k
    def singleNumber2(self, nums) -> int:

        xor_result = 0
        for x in nums:
            xor_result ^= x
            print(xor_result)
        return xor_result

nums = [2, 2, 1]
a = Solution()
a.singleNumber2(nums)
