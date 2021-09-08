# itertoolsなかったらきつい？
#

import itertools
class Solution:
    def permute(self, nums):# List[List[int]]:
        per = list(itertools.permutations(nums))
        return per

num = [1,2,3]

per = list(itertools.permutations(num))

print(per)


